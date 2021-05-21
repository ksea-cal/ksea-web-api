from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

from api.base.mixins import BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin, BaseCreateModelMixin
from api.base.permissions import BoardCreateOrAllowAny, IsAuthenticated
from api.user.serializers import UserProfileSerializer

from .models import Event
from .serializers import EventSerializer


class EventViewSet(BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin, BaseCreateModelMixin, viewsets.GenericViewSet):
    """Retrieve/List/Create events"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [BoardCreateOrAllowAny,]


class ParticipateEventView(BaseAPIMixin, APIView):
    """Check in to a participant"""
    permission_classes = [IsAuthenticated,]

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        userprofile = request.user.current_profile
        if not userprofile:
            return self.err_response(detail="User does not have a proper profile", status=status.HTTP_403_FORBIDDEN)
        code = request.data.get('code', None)
        if not code:
            return self.err_response(detail="Does not contain the code", status=status.HTTP_400_BAD_REQUEST)
        try:
            event = Event.objects.get(code=code)
        except Event.DoesNotExist:
            return self.err_response(detail="Event is not valid", status=status.HTTP_404_NOT_FOUND)
        if userprofile.semester != event.semester:
            return self.err_response(detail="User profile and events are in different semesters", status=status.HTTP_400_BAD_REQUEST)
        if event.participants.filter(pk=userprofile.pk).exists():
            return self.err_response(detail="User is already checked in for the event", status=status.HTTP_400_BAD_REQUEST)

        event.participants.add(userprofile.pk)
        userprofile.points += event.points
        userprofile.save()
        serializer = UserProfileSerializer(userprofile)
        return self.ok_single_response(result=serializer.data, status=status.HTTP_200_OK)


class ViewEventParticipantsView(BaseAPIMixin, LimitOffsetPagination, APIView):
    """View current participants for an event"""

    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return self.err_response(detail="Event pk is not valid", status=status.HTTP_404_NOT_FOUND)
        queryset = event.participants.all()
        serializer = UserProfileSerializer(self.paginate_queryset(queryset, request), many=True)
        return self.get_paginated_response(serializer.data)
from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

from api.base.mixins import BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin, BaseCreateModelMixin
from api.base.permissions import IsAuthenticated
from api.user.serializers import UserProfileSerializer

from ..models import FGEvent, FGParticipation
from ..serializers import FGEventSerializer


class FGEventViewSet(BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin, BaseCreateModelMixin, viewsets.GenericViewSet):
    """Retrieve/List/Create events"""
    queryset = FGEvent.objects.all()
    serializer_class = FGEventSerializer


class ParticipateFGEventView(BaseAPIMixin, APIView):
    """Check in to a FGEvent"""
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
            fgevent = FGEvent.objects.get(code=code)
            fgparticipation = FGParticipation.objects.get(focus_group=fgevent.focus_group, userprofile=request.user.current_profile)
        except Exception:
            return self.err_response(detail="FGEvent is not valid", status=status.HTTP_404_NOT_FOUND)

        fgevent.check_in_user(userprofile, fgparticipation)
        serializer = UserProfileSerializer(userprofile)
        return self.ok_single_response(result=serializer.data, status=status.HTTP_200_OK)


class ViewFGEventParticipantsView(BaseAPIMixin, LimitOffsetPagination, APIView):
    """View current participants for an FGevent"""

    def get(self, request, pk):
        try:
            event = FGEvent.objects.get(pk=pk)
        except FGEvent.DoesNotExist:
            return self.err_response(detail="Event pk is not valid", status=status.HTTP_404_NOT_FOUND)
        queryset = event.participants.all()
        serializer = UserProfileSerializer(self.paginate_queryset(queryset, request), many=True)
        return self.get_paginated_response(serializer.data)
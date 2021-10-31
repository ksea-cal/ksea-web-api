from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from api.base.permissions import IsAuthenticated
from api.base.mixins import BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin
from api.core.models import User

from ..serializers import UserSerializer, UserDetailSerializer

"""
APIS we need:
1. list all current members (with points and attended meetings and such data)
2. list all alumni
4. list all waiting users
"""


class CurrentUserViewSet(BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin, viewsets.GenericViewSet):
    """Retrieve/List current users (without userprofile)"""
    queryset = User.objects.current_members()
    serializer_class = UserSerializer


class WaitingUserViewSet(BaseAPIMixin, BaseListModelMixin, viewsets.GenericViewSet):
    """List waiting users"""
    queryset = User.objects.waiting_members()
    serializer_class = UserSerializer


class AlumniViewSet(BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin, viewsets.GenericViewSet):
    """Retrieve/List alumni users"""
    queryset = User.objects.alumni_members()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDetailViewSet(BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin, viewsets.GenericViewSet):
    """Retrieve/List current users with userprofile"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
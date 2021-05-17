from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from api.base.mixins import BaseAPIMixin
from api.base.permissions import IsAuthenticated
from api.core.models import User
from ..serializers import UserSerializer

"""
APIS we need:
1. list all current members (with points and attended meetings and such data)
2. list all alumni
3. list and detail search all current members (with the given basic data)
4. list all waiting users
"""


class CurrentUserViewSet(BaseAPIMixin, viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.current_members()
    serializer_class = UserSerializer


class WaitingUserView(BaseAPIMixin, ListModelMixin, APIView):
    queryset = User.objects.waiting_members()
    serializer_class = UserSerializer

from rest_framework import status
from rest_framework.generics import RetrieveAPIView

from api.base.mixins import BaseAPIMixin
from api.base.permissions import IsOwner
from api.core.models import User
from ..serializers import UserSerializer


class CurrentUserView(BaseAPIMixin, RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

from rest_framework import status, viewsets
from rest_framework.views import APIView

from api.base.mixins import BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin
from api.base.permissions import IsAuthenticated
from api.core.models import UserProfile

from ..serializers import UserProfileSerializer


class UserProfileViewSet(BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin, viewsets.GenericViewSet):
    """Retrieve/List user profiles"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
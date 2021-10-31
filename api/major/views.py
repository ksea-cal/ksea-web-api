from rest_framework import status, viewsets

from api.base.mixins import BaseAPIMixin, BaseListModelMixin, BaseCreateModelMixin
from api.base.permissions import SuperCreateOrAllowAny
from api.core.models import Major
from .serializers import MajorSerializer

class MajorViewSet(BaseAPIMixin, BaseListModelMixin, BaseCreateModelMixin, viewsets.GenericViewSet):
    """List/Create majors"""
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = (SuperCreateOrAllowAny,)
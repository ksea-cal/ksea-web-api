from rest_framework import status, viewsets

from api.base.mixins import BaseAPIMixin, BaseListModelMixin, BaseCreateModelMixin
from api.base.permissions import SuperCreateOrAllowAny
from api.core.models import Semester
from .serializers import SemesterSerializer

class SemesterViewSet(BaseAPIMixin, BaseListModelMixin, BaseCreateModelMixin, viewsets.GenericViewSet):
    """List/Create semesters"""
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = (SuperCreateOrAllowAny,)
from rest_framework import viewsets

from api.base.mixins import BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin

from ..models import FocusGroup
from ..serializers import FocusGroupSerializer


class FocusGroupViewSet(BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin, viewsets.GenericViewSet):
    """Retrieve/List/Create events"""
    queryset = FocusGroup.objects.all()
    serializer_class = FocusGroupSerializer

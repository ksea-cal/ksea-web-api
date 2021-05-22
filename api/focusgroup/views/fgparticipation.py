from rest_framework import viewsets

from api.base.mixins import BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin

from ..models import FGParticipation
from ..serializers import FGParticipationSerializer


class FGParticipationViewSet(BaseAPIMixin, BaseListModelMixin, BaseRetrieveModelMixin, viewsets.GenericViewSet):
    """Retrieve/List/Create events"""
    queryset = FGParticipation.objects.all()
    serializer_class = FGParticipationSerializer

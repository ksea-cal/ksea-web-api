from rest_framework import serializers

from ..models import FGParticipation


class FGParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FGParticipation
        fields = '__all__'
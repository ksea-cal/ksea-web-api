from rest_framework import serializers

from ..models import FGEvent

class FGEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = FGEvent
        fields = '__all__'
from rest_framework import serializers

from ..models import FocusGroup


class FocusGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = FocusGroup
        fields = '__all__'
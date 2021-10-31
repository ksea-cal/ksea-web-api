from rest_framework import serializers

from api.core.models import Major


class MajorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Major
        fields = '__all__'

    def create(self, validated_data):
        if Major.objects.filter(**validated_data):
            raise serializers.ValidationError("Major with the same properties already exist")
        major = Major.objects.create(**validated_data)
        return major
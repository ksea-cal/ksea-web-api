from rest_framework import serializers

from api.core.models import Semester


class SemesterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Semester
        fields = '__all__'

    def create(self, validated_data):
        if Semester.objects.filter(**validated_data):
            raise serializers.ValidationError("Semester with the same properties already exist")
        semester = Semester.objects.create(**validated_data)
        return semester
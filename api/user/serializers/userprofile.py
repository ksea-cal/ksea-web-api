from rest_framework import serializers

from api.core.models import UserProfile
from api.semester.serializers import SemesterSerializer


class UserProfileSerializer(serializers.ModelSerializer):

    semester = SemesterSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'
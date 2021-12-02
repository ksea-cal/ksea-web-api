from rest_framework import serializers

from ..models import Event
from api.user.serializers import UserSerializer
from api.semester.serializers import SemesterSerializer


class EventSerializer(serializers.ModelSerializer):

    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    semester = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        model = Event
        fields = '__all__'

    def validate_owner(self):
        return self.context['request'].user

    def validate(self, data):
        if not self.context['request'].user and self.context['request'].user.is_currently_board_member:
            raise serializers.ValidationError("you are currently not a board member")
        data['owner'] = self.context['request'].user.current_profile
        data['semester'] = self.context['request'].user.current_profile.semester
        print(data)
        return data

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        return event


class EventDetailSerializer(serializers.ModelSerializer):

    # owner = UserSerializer()
    semester = SemesterSerializer()

    class Meta:
        model = Event
        fields = '__all__'
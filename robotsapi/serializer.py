from rest_framework import serializers
from .models import RobotFriends


class RobotFriendsSerialized(serializers.ModelSerializer):
    class Meta:
        model = RobotFriends
        fields = "__all__"

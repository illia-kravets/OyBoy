from rest_framework import serializers

from .models import User, Channel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ChannelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    subscribers = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Channel
        fields = "__all__"
    
    def get_subscribers(self, obj):
        if subs := getattr(obj, "subscribers", None):
            return subs
        return 0

    
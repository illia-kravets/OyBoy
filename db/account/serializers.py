from rest_framework import serializers

from .models import Profile



class ProfileSerializer(serializers.ModelSerializer):
    subscribers = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Profile
        fields = "__all__"
    
    def get_subscribers(self, obj):
        if subs := getattr(obj, "subscriber_count", None):
            return subs
        return 0

    
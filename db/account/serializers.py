from pkg_resources import require
from rest_framework import serializers

from .models import Profile



class ProfileSerializer(serializers.ModelSerializer):
    subscriber_count = serializers.SerializerMethodField(read_only=True, required=False)
    subscribtion_count = serializers.SerializerMethodField(read_only=True, required=False)
    
    class Meta:
        model = Profile
        fields = "__all__"
    
    def get_subscriber_count(self, obj):
        if subs := getattr(obj, "subscriber_count", None):
            return subs
        return 0
    
    def get_subscribtion_count(self, obj):
        if subs := getattr(obj, "subscriber_count", None):
            return subs
        return 0


    
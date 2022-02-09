from rest_framework import serializers

from db.account.serializers import ChannelSerializer, UserSerializer

from . import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ["title", "description"]


class ViewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = models.View
        fields = ["user", "video_id"]


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Like
        fields = ["user", "video_id"]


class DislikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Dislike
        fields = ["user", "video_id"]


class FavouriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Favourite
        fields = ["user", "video_id"]


class VideoSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    likes = serializers.SerializerMethodField(read_only=True)
    dislikes = serializers.SerializerMethodField(read_only=True)
    views = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Video
        fields = "__all__"

    def get_likes(self, obj):
        if likes := getattr(obj, "like_count", None):
            return likes
        return 0

    def get_dislikes(self, obj):
        if dislikes := getattr(obj, "dislike_count", None):
            return dislikes
        return 0

    def get_views(self, obj):
        if views := getattr(obj, "view_count", None):
            return views
        return 0


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    dislikes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Comment
        fields = "__all__"

    def get_likes(self, obj):
        if likes := getattr(obj, "like_count", None):
            return likes
        return 0

    def get_dislikes(self, obj):
        if dislikes := getattr(obj, "dislike_count", None):
            return dislikes
        return 0

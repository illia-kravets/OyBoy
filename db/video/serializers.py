from rest_framework import serializers

from db.account.serializers import ChannelSerializer, UserSerializer

from .models import Tag, View, Like, Dislike, Favourite, Video, Tag, Comment, SearchHistory


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["title", "description"]


class ViewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = View
        fields = ["user", "video_id"]


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ["user", "video_id"]


class DislikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Dislike
        fields = ["user", "video_id"]


class FavouriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Favourite
        fields = ["user", "video_id"]


class SearchSerializer(serializers.ModelSerializer):
    searches = serializers.SerializerMethodField(read_only=True)
    searched = serializers.SerializerMethodField(read_only=True)
 
    def get_searches(self, obj):
        if likes := getattr(obj, "search_count", None):
            return likes
        return 0

    def get_searched(self, obj):
        if searched := getattr(obj, "searched", None):
            return searched
        return False

    class Meta:
        model = SearchHistory
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(read_only=True)
    tags = TagSerializer(many=True, required=False)
    likes = serializers.SerializerMethodField(read_only=True)
    dislikes = serializers.SerializerMethodField(read_only=True)
    views = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Video
        fields = "__all__"
    
    
    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        video = super().create(validated_data)
        tags = [Tag(video=video, **x) for x in tags]
        Tag.objects.bulk_create(tags)
        return video

        
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
        model = Comment
        fields = "__all__"

    def get_likes(self, obj):
        if likes := getattr(obj, "like_count", None):
            return likes
        return 0

    def get_dislikes(self, obj):
        if dislikes := getattr(obj, "dislike_count", None):
            return dislikes
        return 0

from rest_framework.viewsets import ModelViewSet
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from . import models
from . import serializers
from .filterset import VideoFilterset, TagFilterset
# Create your views here.


class VideoViewSet(ModelViewSet):
    model_class = models.Video
    serializer_class = serializers.VideoSerializer
    queryset = model_class.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = VideoFilterset
    search_fields = ['name', 'profile__username']
    ordering_fields = ["id", "created_at", "view_count"]

    def get_queryset(self):
        annotations = {
            "like_count": Count('like'),
            "dislike_count": Count("dislike"),
            "view_count": Count("view") 
        }
        return super().get_queryset().annotate(**annotations).prefetch_related("profile", "tags")


class TagViewSet(ModelViewSet):
    model_class = models.Tag
    filterset_class = TagFilterset
    filter_backends = [DjangoFilterBackend]
    serializer_class = serializers.TagSerializer
    queryset = model_class.objects

    def get_queryset(self):
        return super().get_queryset().values("title").annotate(count=Count("id")).order_by("-count")


class SearchHistoryViewSet(ModelViewSet):
    model_class = models.SearchHistory
    serializer_class = serializers.SearchSerializer
    queryset = model_class.objects
    search_fields = ["text"]

    # filterset_class = TagFilterset
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    def get_queryset(self):
        # TODO - add searched
        return super().get_queryset().values("text", "video_type").annotate(search_count=Count("id")).order_by("-search_count")



class CommentViewSet(ModelViewSet):
    model_class = models.Comment
    serializer_class = serializers.CommentSerializer
    queryset = model_class.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'profile__username']
    ordering_fields = ["id", "created_at"]

    def get_queryset(self):
        annotations = {
            "like_count": Count('likes'),
            "dislike_count": Count("dislikes")
        }
        return super().get_queryset().annotate(**annotations)


class FavouriteViewSet(ModelViewSet):
    model_class = models.Favourite
    serializer_class = serializers.FavouriteSerializer
    queryset = model_class.objects.all()


class LikeViewSet(ModelViewSet):
    model_class = models.Like
    serializer_class = serializers.LikeSerializer
    queryset = model_class.objects.all()


class DislikeViewSet(ModelViewSet):
    model_class = models.Dislike
    serializer_class = serializers.DislikeSerializer
    queryset = model_class.objects.all()


class ViewViewSet(ModelViewSet):
    model_class = models.View
    serializer_class = serializers.ViewSerializer
    queryset = model_class.objects.all()

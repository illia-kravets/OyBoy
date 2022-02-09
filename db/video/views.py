from django.db.models.base import Model
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count

from . import models
from . import serializers
# Create your views here.


class VideoViewSet(ModelViewSet):
    model_class = models.Video
    serializer_class = serializers.VideoSerializer
    queryset = model_class.objects.all()

    def get_queryset(self):
        annotations = {
            "like_count": Count('like'),
            "dislike_count": Count("dislike"),
            "view_count": Count("view") 
        }
        return super().get_queryset().annotate(**annotations)


class CommentViewSet(ModelViewSet):
    model_class = models.Comment
    serializer_class = serializers.CommentSerializer
    queryset = model_class.objects.all()

    def get_queryset(self):
        annotations = {
            "like_count": Count('like'),
            "dislike_count": Count("dislike")
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


class TagViewSet(ModelViewSet):
    model_class = models.Tag
    serializer_class = serializers.TagSerializer
    queryset = model_class.objects.all()

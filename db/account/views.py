from django.shortcuts import render
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from db.video.serializers import ViewSerializer 
from db.video.models import View
from db.account.models import Channel
from db.account.serializers import ChannelSerializer
# Create your views here.


class ViewHistoryViewSet(ModelViewSet):
    model_class = View
    serializer_class = ViewSerializer
    queryset = model_class.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
 

class ChannelViewSet(ModelViewSet):
    model_class = Channel
    serializer_class = ChannelSerializer
    queryset = model_class.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ["id", "created_at", "subscriber_count"]

    def get_queryset(self):
        return super().get_queryset().annotate(subscribers=Count('subscriptions')).prefetch_related("user")

# class VideoViewSet(ModelViewSet):
#     model_class = models.Video
#     serializer_class = serializers.VideoSerializer
#     queryset = model_class.objects.all()
#     # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_class = VideoFilterset
#     search_fields = ['name', 'channel__title']
#     ordering_fields = ["id", "created_at", "view_count"]

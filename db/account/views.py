from django.shortcuts import render
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from db.video.serializers import ViewSerializer 
from db.video.models import View
from db.account.models import Profile
from db.account.serializers import ProfileSerializer
# Create your views here.


class ViewHistoryViewSet(ModelViewSet):
    model_class = View
    serializer_class = ViewSerializer
    queryset = model_class.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user)
 

class ChannelViewSet(ModelViewSet):
    model_class = Profile
    serializer_class = ProfileSerializer
    queryset = model_class.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ["id", "created_at", "subscriber_count"]

    def get_queryset(self):
        return super().get_queryset().annotate(subscriber_count=Count('subscribers'))

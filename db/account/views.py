from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from db.video.serializers import ViewSerializer 
from db.video.models import View
# Create your views here.


class ViewHistoryViewSet(ModelViewSet):
    model_class = View
    serializer_class = ViewSerializer
    queryset = model_class.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
 
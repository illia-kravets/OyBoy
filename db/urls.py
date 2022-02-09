from django.urls import path, include
from .video.urls import router as video_router
from .account.urls import router as account_router
from db import account

urlpatterns = [
    path("account/", include(account_router.urls)),
    path("video/", include(video_router.urls)),
]
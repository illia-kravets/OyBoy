from django_filters import rest_framework as filters

from .models import Video, Tag
from . import VideoType

class VideoFilterset(filters.FilterSet):
    tags = filters.BaseInFilter(field_name="tags__title", lookup_expr="in")
    dtype = filters.ChoiceFilter(choices=VideoType.CHOICES)

    class Meta:
        model = Video
        fields = ["tags", "dtype"]


class TagFilterset(filters.FilterSet):
    video_type = filters.MultipleChoiceFilter(field_name="video__dtype", conjoined=True, choices=VideoType.CHOICES)

    class Meta:
        model = Tag
        fields = ["video_type"]
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from db.account.models import BaseModel, User, Channel
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

models.Q

from . import VideoType

class Video(BaseModel):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=524)
    description = models.CharField(max_length=128, null=True, blank=True)
    dtype = models.CharField(max_length=64, choices=VideoType.CHOICES)

    banner = models.ImageField(upload_to='image/', null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name


class Tag(BaseModel):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=524, null=True)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True, related_name="tags")

    def __str__(self) -> str:
        return self.title


class SearchHistory(BaseModel):
    text = models.CharField(max_length=254)
    video_type = models.CharField(max_length=64, choices=VideoType.CHOICES)
    # TODO - user

    def __str__(self) -> str:
        return self.text


class Like(BaseModel):
    user = ForeignKey(User, on_delete=models.SET_NULL, null=True)
    video = ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username + "|" + self.video.name


class Dislike(BaseModel):
    user = ForeignKey(User, on_delete=models.SET_NULL, null=True)
    video = ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username + "|" + self.video.name

    class Meta:
        unique_together = ("user", "video")


class View(BaseModel):
    user = ForeignKey(User, on_delete=models.SET_NULL, null=True)
    video = ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username + "|" + self.video.name

    class Meta:
        unique_together = ("user", "video")


class Favourite(BaseModel):
    user = ForeignKey(User, on_delete=models.CASCADE)
    video = ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username + "|" + self.video.name

    class Meta:
        unique_together = ("user", "video")


class Comment(BaseModel, MPTTModel):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self) -> str:
        return self.name


class CommentLike(BaseModel):
    user = ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")

    def __str__(self) -> str:
        return self.user.username + "|" + self.comment.name

    class Meta:
        unique_together = ("user", "comment")


class CommentDislike(BaseModel):
    user = ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = ForeignKey(Comment, on_delete=models.CASCADE, related_name="dislikes")

    def __str__(self) -> str:
        return self.user.username + "|" + self.comment.name

    class Meta:
        unique_together = ("user", "comment")


class VideoReport(BaseModel):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="reports")
    user = ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    
    def __str__(self) -> str:
        return self.video.name + "|" + self.text[:50]
    

class ChannelReport(BaseModel):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="reports")
    user = ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    
    def __str__(self) -> str:
        return self.channel.title + "|" + self.text[:100]

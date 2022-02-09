from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from db.account.models import BaseModel, User, Channel
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Tag(BaseModel):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=524, null=True)

    def __str__(self) -> str:
        return self.title


class Video(BaseModel):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    url = models.CharField(max_length=128)
    name = models.CharField(max_length=524)
    description = models.CharField(max_length=128, null=True, blank=True)

    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)

    def __str__(self) -> str:
        return self.name


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

    
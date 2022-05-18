from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    
    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.username


class Channel(BaseModel):
    title = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=524, null=True, blank=True)
    avatar = models.ImageField(upload_to="images/", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title



class Subscription(BaseModel):
    user = ForeignKey(User, on_delete=models.CASCADE)
    channel = ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username + "|" + self.channel.title
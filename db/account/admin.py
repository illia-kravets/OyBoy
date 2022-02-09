from django.contrib import admin
from .models import User, Subscription, Channel
from db.video.admin import VideoInline, ViewInline, FavouriteInline, LikeInline, DislikeInline, Video

# Register your models here.

# @admin.register(Subscription)
# class SubscriptionAdmin(admin.ModelAdmin):
#     pass

class SubscriptionInline(admin.TabularInline):
    model = Subscription


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [ViewInline, FavouriteInline, LikeInline, DislikeInline, SubscriptionInline]


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    inlines = [SubscriptionInline, VideoInline]
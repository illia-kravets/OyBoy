from django.contrib import admin
from .models import User, Subscription, Channel
from db.video.admin import VideoInline, ViewInline, FavouriteInline, LikeInline, DislikeInline, Video
from django.db.models import Count
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
    list_display = ["title", "reports_count"]
    inlines = [SubscriptionInline, VideoInline]
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            reports_count=Count('reports'))
    
    def reports_count(self, obj):
        return obj.reports_count
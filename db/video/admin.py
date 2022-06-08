from django.contrib import admin
from .models import (
    Like, Dislike, Favourite, 
    Video, Tag, View,
    Comment, CommentDislike, CommentLike, 
    VideoReport, ChannelReport
)
from django.db.models import Count

from db.account.models import Channel

# Register your models here.


# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Dislike)
# class DislikeAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Favourite)
# class FavouriteAdmin(admin.ModelAdmin):
#     pass


# @admin.register(View)
# class ViewAdmin(admin.ModelAdmin):
#     pass

class ChannelInline(admin.StackedInline):
    model = Channel
    

class LikeInline(admin.TabularInline):
    model = Like


class TagInline(admin.TabularInline):
    model = Tag


class DislikeInline(admin.TabularInline):
    model = Dislike


class ViewInline(admin.TabularInline):
    model = View


class FavouriteInline(admin.TabularInline):
    model = Favourite


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    # inlines = [LikeInline, DislikeInline, ViewInline]
    inlines = [TagInline]
    list_display = ["name", "reports_count"]
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            reports_count=Count('reports'))
    
    def reports_count(self, obj):
        return obj.reports_count



class ChannelInline(admin.StackedInline):
    model = Channel


class VideoInline(admin.StackedInline):
    model = Video

    
@admin.register(VideoReport)
class VideoReportAdmin(admin.ModelAdmin):
    search_fields = ["text", "user__username", "video__name"]
    list_filter = ["video"]
    list_display = ["text", "video", "user"]
    # inlines = [VideoInline]

    
@admin.register(ChannelReport)
class ChannelReportAdmin(admin.ModelAdmin):
    search_fields = ["text", "user__username", "channel__title"]
    list_filter = ["channel"]
    list_display = ["text", "channel", "user"]
    # inlines = [ChannelInline]

# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     pass



# @admin.register(CommentLike)
# class CommentLikeAdmin(admin.ModelAdmin):
#     pass


# @admin.register(CommentDislike)
# class CommentDislikeAdmin(admin.ModelAdmin):
#     pass


# class CommentLikeInline(admin.TabularInline):
#     model = CommentLike


# class CommentDislikeInline(admin.TabularInline):
#     model = CommentDislike


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     inlines = [CommentLikeInline, CommentDislikeInline]


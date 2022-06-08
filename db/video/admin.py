from django.contrib import admin
from .models import (
    Like, Dislike, Favourite, 
    Video, Tag, View,
    Comment, CommentDislike, CommentLike
)

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


class VideoInline(admin.TabularInline):
    model = Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    inlines = [TagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass



# @admin.register(CommentLike)
# class CommentLikeAdmin(admin.ModelAdmin):
#     pass


# @admin.register(CommentDislike)
# class CommentDislikeAdmin(admin.ModelAdmin):
#     pass


class CommentLikeInline(admin.TabularInline):
    model = CommentLike


class CommentDislikeInline(admin.TabularInline):
    model = CommentDislike


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentLikeInline, CommentDislikeInline]


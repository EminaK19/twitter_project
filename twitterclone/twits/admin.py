from django.contrib import admin
from .models import Tweet, TweetLike # Comment, CommentLike


# Register your models here.
admin.site.register(Tweet)
# admin.site.register(Comment)
# admin.site.register(CommentLike)
admin.site.register(TweetLike)

from django import forms
from django.contrib.auth import get_user_model

from .models import Tweet   #, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('tweet_text', 'tweet_image', 'author')
        exclude = ('created_at', 'updated_at')


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('tweet_text', 'tweet_image')


# class NewCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['comment_text']
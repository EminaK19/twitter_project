from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse



class Tweet(models.Model):
    tweet_text = models.TextField(blank=True, null=True)
    tweet_image = models.ImageField(upload_to='tweets', null=True, blank=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='tweets'
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('tweet-detail', kwargs={'pk': self.pk})


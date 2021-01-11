from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse



class Tweet(models.Model):
    tweet_text = models.TextField(blank=True, null=True)
    tweet_image = models.ImageField(upload_to='tweets', null=True, blank=True)
    # author = models.ForeignKey(
    #     get_user_model(), on_delete=models.CASCADE, related_name='tweets'
    #     )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, unique_for_date='created_at')


    class Meta:
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('tweet-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.tweet_text[:20]

    # @property
    # def number_of_comments(self):
    #     return Comment.objects.filter(post_connected=self).count()



# class Comment(models.Model):
#     comment_text = models.TextField(max_length=180)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     # author = models.ForeignKey(
#     #     get_user_model(), on_delete=models.CASCADE, related_name='tweets'
#     #     )
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='details')
#     tweet_connected = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='details')
#     comment_image = models.ImageField(upload_to='comments', null=True, blank=True)
#     active = models.BooleanField(default=True)

#     class Meta:
#         ordering = ('-created_at',)

#     def __str__(self):
#         return 'Comment by {} on {}'.format(self.author, self.tweet_connected)

class TweetLike(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='twlikes', on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='twlikes', on_delete=models.CASCADE)

# class CommentLike(models.Model):
#     user = models.ForeignKey(User, related_name='ctlikes', on_delete=models.CASCADE)
#     comment = models.ForeignKey(Comment, related_name='ctlikes', on_delete=models.CASCADE)




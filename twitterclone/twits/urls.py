from django.urls import path, include

from .views import *


urlpatterns = [
    path('', home_view, name='home-page'),
    path('list/', tweets_list, name='tweets-list'),
    path('<int:pk>/', tweet_detail, name='tweet-detail'),
    path('add/', add_tweet, name='add-tweet'),
    path('update/<int:pk>', update_tweet, name='update-tweet'),
    path('delete/<int:pk>', delete_tweet, name='delete-tweet'),
]
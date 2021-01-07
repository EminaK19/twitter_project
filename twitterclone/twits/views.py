from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Tweet
from .forms import AddPostForm, UpdatePostForm

def home_view(request):
    return HttpResponse('<h1> Welcome to TwitterClone </h1>')


def tweets_list(request):
    tweets = Tweet.objects.all()
    return render(
        request, 'twits/tweets_list.html', {'tweets': tweets}
    )


def tweet_detail(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    return render(
        request, 'twits/tweet_detail.html', {'tweet': tweet}
    )


def add_tweet(request):
    if request.POST:
        tweet_form = AddPostForm(request.POST, request.FILES)
        if tweet_form.is_valid():
            tweet = tweet_form.save()
            return redirect(tweet.get_absolute_url())
    else:
        tweet_form = AddPostForm()
    return render(request, 'twits/add_tweet.html', {'tweet_form': tweet_form})


def update_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    tweet_form = UpdatePostForm(request.POST or None, instance=tweet)
    if tweet_form.is_valid():
        tweet_form.save()
        return redirect(tweet.get_absolute_url())
    return render(request, 'twits/update_tweet.html', {
        'tweet_form': tweet_form,
        'tweet': tweet
    })


def delete_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.method == 'POST':
        tweet.delete()
        return redirect('home-page')
    return render(request, 'twits/delete_tweet.html')
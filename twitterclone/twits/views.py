from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .models import Tweet,  TweetLike   #, # CommentLike, Comment
from .forms import AddPostForm, UpdatePostForm   #, # NewCommentForm




def home_view(request):
    return render(
        request, 'twits/home_page.html'
    )

def loading(request):
    return render(request, 'twits/index.html')



# @login_required
def tweets_list(request):
    tweets_ls = Tweet.objects.all()
    paginator = Paginator(tweets_ls, 4)
    page = request.GET.get('page')
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)

    if request.user.is_authenticated:
        context['liked_post'] = [i for i in tweets_ls if Like.objects.filter(user = self.request.user, post=i)]
    
    return render(
        request, 'twits/tweets_list.html', {'page': page, 'tweets': tweets}
    )

# @login_required
def tweet_detail(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    
    return render(
        request, 'twits/tweet_detail.html', {'tweet': tweet}
    )

# @login_required
def add_tweet(request):
    if request.POST:
        tweet_form = AddPostForm(request.POST, request.FILES)
        if tweet_form.is_valid():
            tweet = tweet_form.save()
            return redirect(tweet.get_absolute_url())
    else:
        tweet_form = AddPostForm()
    return render(request, 'twits/add_tweet.html', {'tweet_form': tweet_form})

# @login_required
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

# @login_required
def delete_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweets-list')
    return render(request, 'twits/delete_tweet.html', {'tweet': tweet})


def search_posts(request):
    query = request.GET.get('p')
    object_list = Tweet.objects.filter(tags__icontains=query)

    return render(request, "twits/search_posts.html")
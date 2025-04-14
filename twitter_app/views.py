from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .twitter_utils import get_twitter_api, get_user_tweets, post_tweet

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tweet')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tweet')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def tweet_view(request):
    if request.method == 'POST':
        tweet_text = request.POST.get('tweet')
        try:
            api = get_twitter_api()
            post_tweet(api, tweet_text)
            return HttpResponse("Tweet posted successfully!")
        except Exception as e:
            return HttpResponse(f"Error posting tweet: {str(e)}")
    return render(request, 'tweet.html')

@login_required
def timeline_view(request):
    try:
        api = get_twitter_api()
        tweets = get_user_tweets(api)
        
        # Format tweets for display
        formatted_tweets = []
        if tweets:
            for tweet in tweets:
                formatted_tweets.append((
                    tweet.author_id,  # Note: This will be the user ID, not username
                    tweet.text
                ))
        
        return render(request, 'timeline.html', {'tweets': formatted_tweets})
    except Exception as e:
        return HttpResponse(f"Error fetching timeline: {str(e)}")

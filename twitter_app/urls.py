# twitter_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tweet/', views.tweet_view, name='tweet'),
    path('timeline/', views.timeline_view, name='timeline'),
]

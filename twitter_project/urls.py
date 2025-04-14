# twitter_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('twitter_app.urls')),  # This includes app-level URLs
]

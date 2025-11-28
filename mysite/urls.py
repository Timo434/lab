# mysite/urls.py
from django.urls import path, include

urlpatterns = [
    # ...
    path(r'', include('app_blog.urls')),
]
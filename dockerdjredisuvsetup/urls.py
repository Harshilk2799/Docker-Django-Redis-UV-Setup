from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", FetchPostsAPIView.as_view(), name="fetch-posts")
]

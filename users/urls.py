from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from users.views import UserListCreateView, UserDetailView

urlpatterns = [
    path('list/', UserListCreateView.as_view()),
    path('update/<int:pk>/', UserDetailView.as_view()),

]
# urlpatterns = format_suffix_patterns(urlpatterns)
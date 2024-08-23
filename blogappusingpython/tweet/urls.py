from django.urls import path
from django.shortcuts import render
from .views import tweet_list, tweet_create, tweet_delete, tweet_edit, register

urlpatterns = [
    path("", tweet_list, name="tweet_list"),
    path("create/", tweet_create, name="tweet_create"),
    path("<int:tweet_id>/edit/", tweet_edit, name="tweet_edit"),
    path("<int:tweet_id>/delete/", tweet_delete, name="tweet_delete"),
    path("register/", register, name="register"),
]

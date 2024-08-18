from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path("",views.gtaIV, name="GtaIv"),
]
     



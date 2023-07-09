from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home-page', views.HomePage, name='HomePage'),
    path('feature-page', views.FeaturePage, name='FeaturePage'),
    path('', views.MainPage, name='MainPage')
]

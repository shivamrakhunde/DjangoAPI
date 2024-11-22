from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
     path('hello/', views.HelloWorldView.as_view(), name='helloworld'),
]
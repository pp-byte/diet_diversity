from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name= 'include'),

    path('index',views.index, name= 'index'),
]
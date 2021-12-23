from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    # path('',views.index, name= 'include'),
    # path('',views.include, name= 'include'),
    path('index/',views.index, name= 'index'),
    path('login/', views.login_request, name='login'),
    # path('sign/', views.login_request, name='sign'),
    path('logout/',views.logout, name='logout'),
    path('register/', views.register_request, name='register'),
    path('new_recipe/',views.new_recipe,name='new_recipe'),
    path('captwellpic/', views.captwellpic, name='captwellpic'),
    path('uploadwellpic/', views.uploadwellpic, name='uploadwellpic'),
    path('language/',views.language,name='language'),
    path('',views.about,name='about'),
    
]
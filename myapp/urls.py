from .views import signup, login, logout, home
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]


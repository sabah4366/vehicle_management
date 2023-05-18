from django.contrib import admin
from django.urls import path
from .views import signup,signin,signout,admin_register

urlpatterns = [
    path('',signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('signout/',signout,name='signout'),
    path('register/',admin_register,name='register')

] 

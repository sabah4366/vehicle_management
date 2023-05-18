from django.contrib import admin
from django.urls import path
from .views import home,vehicle_create,vehicle_update,delete_vehicle

urlpatterns = [
    
    path('create/vehicle/',vehicle_create,name='create-vehicle'),
    path('update/<int:pk>/vehicle/',vehicle_update,name='update-vehicle'),
    path('delete/<int:pk>/vehicle/',delete_vehicle,name='delete-vehicle'),
    path('home/',home,name='home')

] 

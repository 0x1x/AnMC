from django.contrib import admin
from django.urls import path,re_path,include
from . import views


urlpatterns = [
    path('index/', views.index, name='AnMC_index'),
]
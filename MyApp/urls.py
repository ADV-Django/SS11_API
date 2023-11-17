
from django.contrib import admin
from django.urls import path

from MyApp import views

urlpatterns = [
    path('api/v1/category/index',views.index),
    path('api/v1/category/save', views.store),
    path('api/v1/category/findById/<id>', views.findById),
    path('api/v1/category/findByName', views.findByName),
    path('api/v1/category/deleteById/<id>', views.deleteById),
    path('api/v1/category/updateById/<id>', views.updateById),
]

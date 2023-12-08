from django.urls import path

from MyApp.controllers import views, product_views, sale_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('api/v1/category/index', views.index),
    path('api/v1/category/save', views.store),
    path('api/v1/category/findById/<id>', views.findById),
    path('api/v1/category/findByName', views.findByName),
    path('api/v1/category/deleteById/<id>', views.deleteById),
    path('api/v1/category/updateById/<id>', views.updateById),
    #------------Route Product------------------------------
    path('api/v1/product/index', product_views.index),
    path('api/v1/product/save', product_views.store),
    path('api/v1/product/findById/<id>', product_views.findById),
    path('api/v1/product/findByName', product_views.findByName),
    path('api/v1/product/deleteById/<id>', product_views.deleteById),
    path('api/v1/product/updateById/<id>', product_views.updateById),
    path('api/v1/sale',sale_views.commit_data),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



]

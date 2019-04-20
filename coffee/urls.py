# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from menu import views
from order import views as order_views

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'order', order_views.OrderViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

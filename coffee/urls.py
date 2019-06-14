# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from menu import views as menu_views
from order import views as order_views


router = DefaultRouter()
router.register(r'menu', menu_views.MenuViewSet)
router.register(r'order', order_views.OrderViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/kakao/login/', order_views.oauthCode),
    # path('accounts/kakao/login/callback/', order_views.oauthCodeCallback),
    # path('accounts/kakao/logout/', order_views.oauthLogOut),
    # path('accounts/kakao/check/', order_views.oauthLogOut),
    path('', include(router.urls)),
]

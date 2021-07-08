from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop import views
from order import views as order_views

router = DefaultRouter()
router.register(r'home', views.MenuViewSet)
router.register(r'orders', order_views.OrderViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

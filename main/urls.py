"""health_check_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
import main.views as main_views
import main.API.viewsets as main_viewsets

router = DefaultRouter()
router.register(r'health_check', main_viewsets.HealthCheckViewSet)
router.register(r'my_health_checks', main_viewsets.OwnHealthCheckViewSet)
router.register(r'users', main_viewsets.UserViewSet)


urlpatterns = [
    path('', main_views.home_view, name='home'),
    path('register/', main_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('api/', include(router.urls)),
]
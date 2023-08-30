"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.db import router
from django.urls import include, path
from django.urls import path
from rest.views import KurulusViewSet, LoginView, RegisterView, SubscribeViewSet, KurulusListView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'kurulus', KurulusViewSet)
router.register(r'takip', SubscribeViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),

    # auth urls
    path('auth/register/', RegisterView.as_view(), name='register-api'),
    path('auth/login/', LoginView.as_view(), name='login-api'),

    # rest urls
    path('rest/', include(router.urls)),
    path('rest/kuruluslist', KurulusListView.as_view()),


    
]

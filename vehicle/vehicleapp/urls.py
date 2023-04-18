"""vehicle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('',views.table,name='table'),
    path('form1',views.form1,name='form1'),
    path('form',views.form,name='form'),
    path('login1',views.login1,name='login1'),
    path('user',views.user,name='user'),
    path('add',views.add,name='add'),
    path('super',views.super,name='super'),
    path('product', views.product, name='product'),
    path('pro', views.pro, name='pro'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('logout',views.logout, name='logout'),


]

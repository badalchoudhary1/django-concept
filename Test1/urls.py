"""
URL configuration for Test1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# Test1/urls.py
from django.contrib import admin
from django.urls import path
from web import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home,name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('filter/',views.filter,name='filter'),
    path("search/",views.search),
    path("show/",views.show),
    path("register/",views.register),
    path('login/',views.login,name='login'),
    path('landing/',views.index),
    path('deletecookie/',views.deletecookie,name='deletecookie'),
    path('setcookie/',views.setcookies,name='setcookie'),
    path('getcookie/',views.setcookies,name='getcookie')
]





"""
URL configuration for eduHub project.

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
from django.contrib import admin
from django.urls import path , include

admin.site.site_header = "Fluentify Admin"
admin.site.site_title = "Fluentify Admin Portal"
admin.site.index_title = "Welcome to Fluentify Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('home.urls')),
    path("home/", include('home.urls')),
    path("abt2/", include('home.urls')),
    path("register/", include('home.urls')),
    path("contact/", include('home.urls')),
    path("checker/", include('home.urls')),
    path("courses/", include('home.urls')),
    path("servicepage/", include('home.urls')),
    path("exam/", include('home.urls')),
    path("teachers/", include('home.urls')),
    path("teacher_profile/", include('home.urls')),
    path("chat/", include('home.urls')),
    path("playlist/", include('home.urls')),
    path("error_checking/", include('home.urls')),
    path("profile/", include('home.urls')),
    path("update/", include('home.urls')),
    path("login/", include('home.urls')),
]

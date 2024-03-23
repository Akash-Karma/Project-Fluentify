from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("contact", views.contact, name='contact'),
    path("home", views.home, name='home'),
    path("abt2", views.abt2, name='abt2'),
    path("register", views.register, name='register'),
    path("checker", views.register, name='checker'),
    path("courses", views.courses, name='courses'),
    path("servicepage", views.servicepage, name='servicepage'),
    path("exam", views.exam, name='exam'),
    path("teachers", views.teachers, name='teachers'),
    path("teacher_profile", views.teacher_profile, name='teacher_profile'),
    path("chat", views.chat, name='chat'),
]

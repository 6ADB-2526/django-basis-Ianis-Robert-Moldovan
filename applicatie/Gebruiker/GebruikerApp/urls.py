from django.urls import path
from . import views

urlpatterns = [
    path('/GebruikerApp/login', views.say_welkom)
]
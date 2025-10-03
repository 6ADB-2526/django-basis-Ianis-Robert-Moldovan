from django.urls import path
from . import views

urlpatterns = [
    path('opstart/', views.opstart)
]
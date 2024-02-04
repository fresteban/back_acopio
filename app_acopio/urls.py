from django.urls import path
from . import views

urlpatterns = [
    path('wena/', views.wena),
]

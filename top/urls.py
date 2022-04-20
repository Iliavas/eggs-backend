from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ListCreateTop


urlpatterns = [
    path("top", ListCreateTop.as_view())
]

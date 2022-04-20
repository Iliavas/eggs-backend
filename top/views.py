from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from .serializers import TopSerializer
from .models import Top
from rest_framework.routers import DefaultRouter


class ListCreateTop(ListCreateAPIView):
    serializer_class = TopSerializer
    queryset = Top.objects.all()


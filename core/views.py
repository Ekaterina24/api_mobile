from django.shortcuts import render
from core.serializer import EventSerializer
from rest_framework import generics
from core.models import *
from rest_framework.viewsets import ModelViewSet

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

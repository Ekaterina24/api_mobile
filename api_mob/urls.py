from django.contrib import admin
from django.urls import path
from core.views import EventViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'events', EventViewSet, basename='events')

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls

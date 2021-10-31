from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MajorViewSet


app_name = 'major'

router = DefaultRouter()
router.register('', MajorViewSet)

urlpatterns = [
    path('', include(router.urls))
]
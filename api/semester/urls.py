from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SemesterViewSet


app_name = 'semester'

router = DefaultRouter()
router.register('', SemesterViewSet)

urlpatterns = [
    path('', include(router.urls))
]
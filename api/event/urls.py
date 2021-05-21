from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EventViewSet, ParticipateEventView, ViewEventParticipantsView


router = DefaultRouter()
router.register('', EventViewSet)

app_name = 'event'

urlpatterns = [
    path('participate/', ParticipateEventView.as_view(), name="participate"),
    path('<int:pk>/participants/', ViewEventParticipantsView.as_view(), name="participants"),
    path('', include(router.urls)),
]
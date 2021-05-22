from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FGEventViewSet, FocusGroupViewSet, ViewFGEventParticipantsView, ParticipateFGEventView


router = DefaultRouter()
router.register('', FocusGroupViewSet)
router.register('events', FGEventViewSet)


app_name = 'event'

urlpatterns = [
    path('participate/', ParticipateFGEventView.as_view(), name="participate"),
    path('<int:pk>/participants/', ViewFGEventParticipantsView.as_view(), name="participants"),
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AlumniViewSet, SignupView, LoginView,
    CurrentUserViewSet, WaitingUserViewSet, UserDetailViewSet,
    UserProfileViewSet
)

app_name = 'user'


router = DefaultRouter()
router.register('alumni-users', AlumniViewSet)
router.register('current-users', CurrentUserViewSet)
router.register('waiting-users', WaitingUserViewSet)
router.register('detailed-users', UserDetailViewSet)
router.register('user-profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name='signup'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SignupView, LoginView, CurrentUserViewSet, WaitingUserView


app_name = 'user'


router = DefaultRouter()
router.register('current-users', CurrentUserViewSet)

print(router.urls)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name='signup'),
    path('waiting-users/', WaitingUserView.as_view(), name="waiting")
]
from django.urls import path, include

from .views import SignupView, LoginView


app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name='signup')
]
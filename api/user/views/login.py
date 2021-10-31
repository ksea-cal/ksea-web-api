from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from api.base.mixins import BaseAPIMixin
from api.core.models import User
from ..serializers import UserLoginSerializer, UserDetailSerializer


class LoginView(BaseAPIMixin, ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        """
            log in the user if username/password is valid
            if user blocked/susepnded, return 403
            if invalid username/password, return 400
        """
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return self.err_response('Could not log in to the server', status=status.HTTP_400_BAD_REQUEST)
        user = serializer.validated_data
        user_instance = User.objects.get(pk=user.pk)
        # if not user.status in [User.Status.ACTIVE, User.Status.ALUMNI]:
        #     return self.err_response('User is not currently active', status=status.HTTP_403_FORBIDDEN)
        user_data = UserDetailSerializer(user_instance).data
        token, _ = Token.objects.get_or_create(user=user_instance)
        return self.ok_single_response(result={"token": token.key, "user": user_data}, status=status.HTTP_200_OK)
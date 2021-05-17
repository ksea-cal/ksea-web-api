from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from api.base.mixins import BaseAPIMixin
from ..serializers import UserLoginSerializer


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
        token, _ = Token.objects.get_or_create(user=user)
        return self.ok_single_response(result=token.key, status=status.HTTP_200_OK)
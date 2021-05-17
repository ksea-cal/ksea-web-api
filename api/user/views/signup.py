from rest_framework import status
from rest_framework.views import APIView

from api.base.mixins import BaseAPIMixin
from ..serializers import UserSerializer


class SignupView(BaseAPIMixin, APIView):
    def post(self, request, *args, **kwargs):
        """
            create a user with the given berkeley_email/password
            if email invalid or contains an error, return 400
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.ok_single_response(result=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return self.err_response(message="Invalid login data", status=status.HTTP_400_BAD_REQUEST)
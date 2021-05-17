from rest_framework import status
from rest_framework.response import Response


class BaseAPIMixin:
    """base mixin that standardizes responses"""

    def ok_response(self, message='', results=[], status=status.HTTP_200_OK):
        return Response({
            'success': True,
            'results': results,
            'message': message
        }, status=status)

    def ok_single_response(self, message='', result=None, status=status.HTTP_200_OK):
        return Response({
            'success': True,
            'result': result,
            'message': message
        }, status=status)

    def err_response(self, detail='', status=status.HTTP_400_BAD_REQUEST):
        return Response({
            'detail': detail
        }, status=status)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin


class BaseAPIMixin:
    """Base mixin that standardizes responses"""

    def err_response(self, detail='', status=status.HTTP_400_BAD_REQUEST):
        return Response({
            'detail': detail
        }, status=status)

    def ok_single_response(self, result=None, status=status.HTTP_200_OK):
        return Response(result, status=status)


class BaseListModelMixin(ListModelMixin):
    """Base mixin for listing"""
    pass


class BaseRetrieveModelMixin(RetrieveModelMixin):
    """Base mixin for retrieving"""
    pass


class BaseCreateModelMixin(CreateModelMixin):
    """Base mixin for creating"""
    pass

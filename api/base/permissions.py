from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated, IsAdminUser

from api.core.models import UserProfile

# class IsOwner(BasePermission):
#     """
#     Custom permission to only allow owners of an object to edit it.
#     """
#     def has_permission(self, request, view):
#         return request.user and request.user.is_authenticated
#
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user or request.user.is_superuser == True


class SuperCreateOrAllowAny(BasePermission):
    """Only super user can create but any user can access"""
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user and request.user.is_superuser
        return True


class BoardCreateOrAllowAny(BasePermission):
    """Only board members can create but any user can access"""
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user and request.user.current_profile and request.user.current_profile.role == UserProfile.Role.BOARD_MEMBER
        return True
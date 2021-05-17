from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated


# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         user = request.user
#         if isinstance()
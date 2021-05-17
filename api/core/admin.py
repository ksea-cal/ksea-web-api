from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define auth model for custom User Model without username"""
    fieldsets = (
        (None, {'fields': ('berkeley_email', 'password')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('berkeley_email', 'password', 'is_staff', 'is_active')}
        ),
    )
    ordering = ('berkeley_email',)
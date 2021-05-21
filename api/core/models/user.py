from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Model manager for custom user model"""

    def _create_user(self, berkeley_email, password, **extra_fields):
        """Create and save User with the given email and password"""
        if not berkeley_email or not User.check_berkeley_email_valid(berkeley_email):
            raise ValueError("The given email is invalid")
        berkeley_email = self.normalize_email(berkeley_email)
        user = self.model(berkeley_email=berkeley_email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, berkeley_email, password, **extra_fields):
        """Create and save a new member User with the given email and password"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(berkeley_email, password, **extra_fields)

    def create_superuser(self, berkeley_email, password, **extra_fields):
        """Create and save a new superuser with the given email and password"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('status', User.Status.ACTIVE)
        return self._create_user(berkeley_email, password, **extra_fields)

    def current_members(self):
        return self.filter(status=User.Status.ACTIVE)

    def waiting_members(self):
        return self.filter(status=User.Status.WAITING)

    def alumni_members(self):
        return self.filter(status=User.Status.ALUMNI)


class User(AbstractUser):
    """Base user model for KSEA"""

    class Status(models.TextChoices):
        ACTIVE = 'ACT', 'Active'
        ALUMNI = 'ALU', 'Alumni'
        WAITING = 'WAI', 'Waiting'
        SUSPENDED = 'SUS', 'Suspended'
        BANNED = 'BAN', 'Banned'

    username = None
    berkeley_email = models.EmailField(unique=True)
    status = models.CharField(max_length = 3, choices=Status.choices, default=Status.WAITING)

    USERNAME_FIELD = 'berkeley_email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        db_table = 'users'

    def check_berkeley_email_valid(email):
        return email.endswith('berkeley.edu')

    @property
    def current_profile(self):
        """Return the most recent profile of the user"""
        from .userprofile import UserProfile
        return UserProfile.objects.current_profile_for_user(self)

    def create_new_profile(self, semester, role):
        """create a new profile for the given semester if the user is valid and no profile exists for the semester"""
        if self.status != self.Status.ACTIVE:
            return None
        from .userprofile import UserProfile
        if UserProfile.objects.filter(user=self, semester=semester):
            return None
        return UserProfile.objects.create(user=self, semester=semester, role=role)

    def is_currently_board_member(self):
        from .userprofile import UserProfile
        return self.current_profile and self.current_profile.role == UserProfile.Role.BOARD_MEMBER
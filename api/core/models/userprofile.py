from django.db import models

from .user import User
from .semester import Semester


class UserProfileManager(models.Manager):
    def current_profile_for_user(self, user):
        return self.filter(user=user).order_by('-semester__pk').first()


class UserProfile(models.Model):
    """Each user's semester profile model"""

    class Role(models.TextChoices):
        GENERAL_MEMBER = 'GEN', 'General member'
        BOARD_MEMBER = 'BOA', 'Board member'

    user = models.ForeignKey(User, related_name="user_profiles", on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, related_name="user_profiles", on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    role = models.CharField(max_length=3, choices=Role.choices, default=Role.GENERAL_MEMBER)
    paid_membership_fee = models.BooleanField(default=False)

    objects = UserProfileManager()

    class Meta:
        db_table = 'user_profiles'
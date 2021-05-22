from django.db import models

from api.core.models import UserProfile, Semester


class FocusGroupManager(models.Model):
    pass

class FocusGroup(models.Model):
    """Model for each focus group"""
    name = models.CharField(max_length=200)
    leaders = models.ManyToManyField(UserProfile, related_name="leading_focus_groups")
    members = models.ManyToManyField(UserProfile, through='FGParticipation', related_name="joined_focus_groups")
    semester = models.ForeignKey(Semester, related_name="focus_groups", on_delete=models.CASCADE)
    number_of_events = models.IntegerField(default=0)
    processed = models.BooleanField(default=False)

    objects = FocusGroupManager()

    class Meta:
        db_table = 'focus_groups'
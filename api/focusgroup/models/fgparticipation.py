from django.db import models

from api.core.models import UserProfile

from .focusgroup import FocusGroup


class FGParticipationManager(models.Manager):
    pass


class FGParticipation(models.Model):
    """ManytoMany model with participations for each FG-user relation"""

    member = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    focus_group = models.ForeignKey(FocusGroup, on_delete=models.CASCADE)
    number_of_participated_events = models.IntegerField(default=0)

    objects = FGParticipationManager()

    class Meta:
        db_table = 'fg_participations'
import uuid

from django.db import models

from api.core.models import UserProfile

from .focusgroup import FocusGroup


class FGEventManager(models.Manager):
    pass


class FGEvent(models.Model):
    """Event model for each FG event"""

    focus_group = models.ForeignKey(FocusGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    participants = models.ManyToManyField(UserProfile, blank=True)
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        db_table = 'fg_event'

    def check_in_user(self, userprofile, fgparticipation):
        self.participants.add(userprofile.pk)
        fgparticipation.number_of_participated_events += 1
        fgparticipation.save()
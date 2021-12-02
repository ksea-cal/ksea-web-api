import random
import string

from django.db import models

from api.core.models import UserProfile, Semester


class EventManager(models.Manager):
    pass


class Event(models.Model):
    """Event model for each KSEA event"""

    class Types(models.TextChoices):
        GM = 'gm', 'general meeting'
        SOCIAL = 'social', 'social'
        NONE = 'none', 'none'

    name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=20, choices=Types.choices)
    points = models.IntegerField(default=0)
    required = models.BooleanField(default=False)
    owner = models.ForeignKey(UserProfile, related_name="created_events", on_delete=models.CASCADE)
    participants = models.ManyToManyField(UserProfile, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    processed = models.BooleanField(default=False)
    semester = models.ForeignKey(Semester, related_name="events", on_delete=models.CASCADE)
    code = models.CharField(max_length=6, default=''.join(random.choice(string.digits) for x in range(6)))
    description = models.TextField(max_length=300)

    objects = EventManager()

    class Meta:
        db_table = 'events'

    def check_in_user(self, userprofile):
        self.participants.add(userprofile.pk)
        userprofile.points += self.points
        userprofile.save()

from django.db import models

from .userprofile import UserProfile


class LogManager(models.Manager):
    pass


class Log(models.Model):
    owner = models.ForeignKey(UserProfile, related_name="logs", on_delete=models.CASCADE)

    objects = LogManager()

    class Meta:
        db_table = 'logs'
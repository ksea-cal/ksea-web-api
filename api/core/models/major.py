from django.db import models


class MajorManager(models.Manager):
    pass

class Major(models.Model):
    """Semester model for each semester"""
    major = models.CharField(max_length=30, unique=True)

    objects = MajorManager()

    class Meta:
        db_table = 'majors'
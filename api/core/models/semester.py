from django.db import models


class SemesterManager(models.Manager):
    pass

class Semester(models.Model):
    """Semester model for each semester"""

    class Terms(models.TextChoices):
        SPRING = 'spr', 'spring'
        FALL = 'fal', 'fall'

    year = models.IntegerField()
    term = models.CharField(max_length=3, choices=Terms.choices)

    objects = SemesterManager()

    class Meta:
        db_table = 'semesters'
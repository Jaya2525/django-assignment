from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

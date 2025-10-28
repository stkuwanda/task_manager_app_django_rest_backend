from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=1000, blank=True, default="")
    due_date = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(blank=False, default=False)
    owner = models.ForeignKey(to=User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
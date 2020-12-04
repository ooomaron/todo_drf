from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    @property
    def status(self):     
      now = timezone.now()
      if now < self.deadline:
        return 'open' 
      else:
        return 'expired'
      
    def __str__(self):
      return self.title



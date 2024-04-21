from django.db import models
from enum import Enum
# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

class Task_status(Enum):
    Not_Started = 'Not Started'
    In_Progress = 'In Progress'
    Completed = 'Completed'

class Task_type(Enum):
    Study = 'Study'
    Work = 'Work'
    Home = 'Home'
    Other = "Other"

class Goal(models.Model):
    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Goal, self).save(*args, **kwargs)
    user=models.ForeignKey(Account, on_delete=models.CASCADE)
    goalTitle = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in Task_status], default=Task_status.Not_Started.value)
    type = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in Task_type], default=Task_type.Other.value)

class Subgoal(models.Model):
    goal = models.ForeignKey(Goal, related_name='subgoals', on_delete=models.CASCADE)
    subgoalTitle = models.CharField(max_length=100)
    timelineDate = models.CharField(max_length=100)
    timelineTime = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)


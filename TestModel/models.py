from django.db import models
from enum import Enum
# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

class Task_status(Enum):
    Not_Started = 'Not started'
    In_Progress = 'In progress'
    Done = 'Done'

class Task_type(Enum):
    Study = 'Study'
    Work = 'Work'
    Entertainment = 'Entertainment'
    Other = "Other"

class Goal(models.Model):
    user=models.ForeignKey(Account, on_delete=models.CASCADE)
    goalTitle = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=[(tag, tag.value) for tag in Task_status],default=Task_status.Not_Started)
    type = models.CharField(max_length=100, choices=[(tag, tag.value) for tag in Task_status],default=Task_type.Other)

class Subgoal(models.Model):
    goal = models.ForeignKey(Goal, related_name='subgoals', on_delete=models.CASCADE)
    subgoalTitle = models.CharField(max_length=100)
    timelineDate = models.CharField(max_length=100)
    timelineTime = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)


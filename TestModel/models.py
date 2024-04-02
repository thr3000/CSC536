from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

class Goal(models.Model):
    user=models.ForeignKey(Account, on_delete=models.CASCADE)
    goalTitle = models.CharField(max_length=100)
    timelineDate = models.CharField(max_length=100)
    timelineTime = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

class Subgoal(models.Model):
    goal = models.ForeignKey(Goal, related_name='subgoals', on_delete=models.CASCADE)
    subgoalTitle = models.CharField(max_length=100)
    timelineDate = models.CharField(max_length=100)
    timelineTime = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)


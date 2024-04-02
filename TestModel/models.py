from django.db import models
from django.core.validators import MinLengthValidator

'''
# Create your models here.
class Goals(models.Model):
    goalTitle = models.CharField(
        max_length=100
    )
    subgoals = models.CharField(
        max_length=100
    )
    timelineDate = models.CharField(
        max_length=100
    )
    timelineTime = models.CharField(
        max_length=100
    )

class Account(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
'''

class User(models.Model):
    user_id = models.AutoField(
        primary_key = True
    )
    username = models.CharField(
        max_length = 16, 
        validators = [MinLengthValidator(5)], 
        unique = True, 
        null = False
    )
    email = models.EmailField(
        unique = True, 
        null = True
    )
    password = models.CharField(
        max_length = 32
    )

class Goal(models.Model):
    goal_id = models.AutoField(
        primary_key = True
    )
    user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE
    )
    title = models.CharField(
        max_length = 64
    )
    date_created = models.DateTimeField(
        auto_now_add = True
    )
    description = models.CharField(
        max_length = 256
    )
    has_completed = models.BooleanField(
        default = False
    )
    
class SubGoal(models.Model):
    subgoal_id = models.AutoField(
        primary_key = True
    )
    goal = models.ForeignKey(
        Goal, on_delete = models.CASCADE
    )
    deadline = models.DateField()
    description = models.CharField(
        max_length = 256
    )
    has_completed = models.BooleanField(
        default = False
    )
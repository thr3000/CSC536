from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
'''
class Account(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

class Goal(models.Model):
    user=models.ForeignKey(Account, on_delete=models.CASCADE)
    goalTitle = models.CharField(max_length=100)
    
    completed = models.BooleanField(default=False)

class Subgoal(models.Model):
    goal = models.ForeignKey(Goal, related_name='subgoals', on_delete=models.CASCADE)
    subgoalTitle = models.CharField(max_length=100)
    timelineDate = models.CharField(max_length=100)
    timelineTime = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
'''


class Account(models.Model):
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
    CATEGORY_CHOICES = [
        ('long_term', 'Long Term'),
        ('short_term', 'Short Term'),
        ('study', 'For Study'),
        ('work', 'For Work'),
    ]
    STATUS_CHOICES = [
        ('not_started_yet', 'Not Started Yet'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(Account, on_delete = models.CASCADE)
    goalTitle = models.CharField(max_length = 64)
    description = models.CharField(max_length = 256, null = True)
    progress = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)])
    category = models.CharField(max_length = 20, choices = CATEGORY_CHOICES, default = 'long_term')
    status = models.CharField(max_length = 32, choices = STATUS_CHOICES)
    
class Subgoal(models.Model):
    goal = models.ForeignKey(
        Goal, 
        related_name = 'subgoals',
        on_delete = models.CASCADE
    )
    subgoalTitle = models.CharField(
        max_length = 100
    )
    timelineDate = models.CharField(
        max_length = 100
    )
    timelineTime = models.CharField(
        max_length = 100
    )
    description = models.CharField(
        max_length = 256,
        null = True
    )
    completed = models.BooleanField(
        default = False
    )
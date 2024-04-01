from django.db import models

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

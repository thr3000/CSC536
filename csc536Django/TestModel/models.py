from django.db import models

# Create your models here.
class Goals(models.Model):
    create_date = models.CharField(
        max_length=100
    )
    content = models.CharField(
        max_length=100
    )

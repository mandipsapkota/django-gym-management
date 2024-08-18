from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=20)
    detail = models.TextField()

    
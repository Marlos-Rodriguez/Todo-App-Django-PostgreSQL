from django.db import models

# Create your models here.


class todos(models.Model):
    content = models.TextField(blank=True, null=True)

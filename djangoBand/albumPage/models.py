from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length = 200)
    band = models.CharField(max_length = 200)
    year = models.SmallIntegerField()

    def __str__(self):
        return self.title

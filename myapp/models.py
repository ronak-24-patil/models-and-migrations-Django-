from django.db import models

class Menuitems(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  # Changed from "course"
    year = models.IntegerField()

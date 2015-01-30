from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=256)

class Player(models.Model):
    position = models.ForeignKey(Position)
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=256)
    team_name = models.CharField(max_length=64)
    team_url  = models.URLField(max_length=256)
    team_code = models.CharField(max_length=3)
    birthdate = models.DateField()

from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=100)

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

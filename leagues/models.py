from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

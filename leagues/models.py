from django.db import models

# Create your models here.
class League(models.Model):
    league_name = models.CharField(max_length=100)

    def __str__(self):
        return self.league_name

class Season(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    date_start = models.DateField()

    def __str__(self):
        return f'{self.league.league_name} {self.date_start}'

class Division(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    division_number = models.IntegerField()

    def __str__(self):
        return f'Division {self.division_number}'

class Team(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Fixture(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    home_score = models.IntegerField()
    away_score = models.IntegerField()
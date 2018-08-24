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
        return f'{self.season.league.league_name} - Division {self.division_number}'

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
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_fixtures')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_fixtures')
    date = models.DateField()

    def __str__(self):
        return f'{self.home_team.team_name} vs. {self.away_team.team_name}'

class Match(models.Model):
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    home_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='home_matches')
    away_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='away_matches')

class Game(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    game_number = models.IntegerField()
    home_score = models.IntegerField()
    away_score = models.IntegerField()
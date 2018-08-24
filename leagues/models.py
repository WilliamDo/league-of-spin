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

    def count_matches_for(self):
        return sum([fixture.get_home_score() for fixture in self.home_fixtures.all()]) + sum([fixture.get_away_score() for fixture in self.away_fixtures.all()])

    
    def count_matches_against(self):
        return sum([fixture.get_away_score() for fixture in self.home_fixtures.all()]) + sum([fixture.get_home_score() for fixture in self.away_fixtures.all()])

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

    def get_home_score(self):
        matches_won = [m for m in self.match_set.all() if m.get_winner() in self.home_team.player_set.all()]
        return len(matches_won)

    def get_away_score(self):
        matches_won = [m for m in self.match_set.all() if m.get_winner() in self.away_team.player_set.all()]
        return len(matches_won)

class Match(models.Model):
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    home_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='home_matches')
    away_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='away_matches')

    def get_winner(self):
        home_games = 0
        away_games = 0
        for game in self.game_set.all():
            if game.home_score > game.away_score:
                home_games += 1
            else:
                away_games += 1

        # FIXME This ia a bug because what if games are equal?
        if home_games > away_games:
            return self.home_player
        else:
            return self.away_player

class Game(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    game_number = models.IntegerField()
    home_score = models.IntegerField()
    away_score = models.IntegerField()
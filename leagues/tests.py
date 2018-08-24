from django.test import TestCase

from .models import Fixture, Match, Team

# Create your tests here.

class FooTests(TestCase):
    fixtures = ['dev']

    def test_get_winner_home(self):
        match = Match.objects.get(pk=1)
        winner = match.get_winner()
        self.assertEqual(winner.first_name, 'Matt')

    def test_get_winner_away(self):
        match = Match.objects.get(pk=9)
        winner = match.get_winner()
        self.assertEqual(winner.first_name, 'Mike')

    def test_fixture_get_score(self):
        fixture = Fixture.objects.get(pk=1)
        self.assertEqual(fixture.get_home_score(), 8)
        self.assertEqual(fixture.get_away_score(), 1)

    def test_team_count_matches(self):
        team = Team.objects.get(pk=1)
        self.assertEqual(team.count_matches_for(), 8)
        self.assertEqual(team.count_matches_against(), 1)

        team = Team.objects.get(pk=2)
        self.assertEqual(team.count_matches_for(), 1)
        self.assertEqual(team.count_matches_against(), 8)
        
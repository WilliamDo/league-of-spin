from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Division, Fixture, League

# Create your views here.
def index(request):
    return HttpResponse("This is the leagues index.")

def table(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    teams = division.team_set.all()
    sorted_teams = sorted(teams, key=lambda t: t.count_matches_for(), reverse=True)
    return render(request, 'leagues/table.html', {'teams': sorted_teams})

class FixtureView(generic.DetailView):
    model = Fixture
    template_name = 'leagues/fixture.html'

class LeagueView(generic.DetailView):
    model = League
    template_name = 'leagues/league.html'
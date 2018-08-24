from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Division

# Create your views here.
def index(request):
    return HttpResponse("This is the leagues index.")

def table(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    teams = division.team_set.all()
    sorted_teams = sorted(teams, key=lambda t: t.count_matches_for(), reverse=True)
    return render(request, 'leagues/table.html', {'teams': sorted_teams})
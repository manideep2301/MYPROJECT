from django.shortcuts import render
from .models import Team, Player, Match, Event
import datetime
from django.shortcuts import render, get_object_or_404
from .models import Team, Player


def list_teams(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': teams})

def list_players(request):
    players = Player.objects.all()
    return render(request, 'players.html', {'players': players})

def list_matches(request):
    matches = Match.objects.all()
    return render(request, 'matches.html', {'matches': matches})

def upcoming_events(request):
    events = Event.objects.filter(date__gte=datetime.date.today()).order_by('date')
    return render(request, 'events.html', {'events': events})

def home(request):
    return render(request, 'home.html')


def team_players(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = Player.objects.filter(team=team)
    return render(request, 'team_players.html', {'team': team, 'players': players})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teams/', views.list_teams, name='list_teams'),
    path('players/', views.list_players, name='list_players'),
    path('matches/', views.list_matches, name='list_matches'),
    path('events/', views.upcoming_events, name='upcoming_events'),
    path('team/<int:team_id>/players/', views.team_players, name='team_players'),
   

]

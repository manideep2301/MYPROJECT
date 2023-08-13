from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    date = models.DateField()
    winner = models.ForeignKey(Team, related_name='winner', null=True, on_delete=models.SET_NULL)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)

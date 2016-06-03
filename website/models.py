from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):

	name = models.CharField(max_length=100)
	manager = models.ForeignKey(User)

	def __str__(self):
		return self.name

class Player(models.Model):

	name = models.CharField(max_length=100)
	position = models.CharField(max_length=40)
	country = models.CharField(max_length=100)
	realLife_team = models.CharField(max_length=50)
	team = models.ForeignKey(Team)

	def __str__(self):
		return self.name

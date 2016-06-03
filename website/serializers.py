from rest_framework import serializers
from .models import Team,Player
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id','username','email','password']


class TeamSerializer(serializers.ModelSerializer):
	manager = UserSerializer()

	class Meta:
		model = Team
		fields = ('id','name','manager')


class PlayerSerializer(serializers.ModelSerializer):
	team = TeamSerializer()

	class Meta:
		model = Player
		fields = ('id','name','position', 'country', 'realLife_team', 'team')


from django import forms
from django.forms import ModelForm
from .models import Player,Team
from django.forms import extras
from django.contrib.auth.models import User
from djangular.forms import NgModelFormMixin, NgModelForm

class TeamForm(ModelForm):
	name = forms.CharField(label='name',max_length=100)
	manager = forms.CharField(label='manager',max_length=40)

	class Meta:
		model = Team
		fields = ['name','manager']


class UserForm(NgModelFormMixin, NgModelForm):
	class Meta:
		model = User
		fields = ['username','email','password']


class PlayerForm(ModelForm):
	name = forms.CharField(label='name',max_length=100)
	position = forms.CharField(label='position',max_length=40)
	country = forms.CharField(label='country',max_length=100)
	realLife_team = forms.CharField(label='realLife_team',max_length=50)
	team = forms.CharField(label='team',max_length=100)

	class Meta:
		model = Player
		fields = ['name','position','country','realLife_team','team']

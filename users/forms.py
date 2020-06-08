from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
	genre_choices = (('boy', 'boy'), ('girl', 'girl'))
	annee_choices = (('second', 'second'), ('third', 'third'))
	genre = forms.ChoiceField(choices=genre_choices, required=True)
	annee = forms.ChoiceField(choices=annee_choices, required=True)

	class Meta:
		model = User 
		fields = ('username', 'genre', 'annee', 'first_name', 'last_name', 'password1', 'password2')
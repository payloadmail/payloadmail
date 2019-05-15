from django import forms
from django.db import models
import pam

class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'password')

	def validate(self):
		if not self.is_valid():
			return False
		user = self.cleaned_data.get('username')
		passwd = self.cleaned_data.get('password')
		p = pam.pam()
		return p.authenticate(user, passwd)

	def get_user_email(self):
		return self.cleaned_data.get('username')
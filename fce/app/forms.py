from django import forms
from django.forms import ModelForm, CharField, Form, PasswordInput, IntegerField, ChoiceField, BooleanField, FileField, Textarea, RadioSelect, EmailField, DateField, FileField #taken from fellowship_application
from django.contrib.auth import authenticate, login, logout
# from app.models import Login
from django.contrib.auth.models import User  #not sure if I need this here



class CustomLoginForm(Form): 
	username = CharField(required=True, max_length=75, label="username")
	password = CharField(widget=PasswordInput(), required=True, max_length=45, label="password")

	# def clean(self):
	# 	email = self.cleaned_data.get('email')[0:30] #replaced 'username' with 'email'
	# 	password = self.cleaned_data.get('password')
	# 	user = authenticate(email=email, password=password)
	# 	if not user or not user.is_active:
	# 		raise forms.ValidationError("That wasn't the right username or password.")
	# 	return self.cleaned_data


class CreateAccountForm(Form):
	username = CharField(required=True, max_length=30, label="Screen Name")  
	first_name = CharField(required=True, max_length=30, label="First Name")
	last_name = CharField(required=True, max_length=30, label="Last Name")
	email = EmailField(required=True, max_length=75, label="Email")
	password = CharField(widget=PasswordInput(), required=True, max_length=45, label="Password")
	retype_password = CharField(widget=PasswordInput(), required=True, max_length=45, label="Retype password")

	def clean_password(self):
		if self.data['password'] != self.data['retype_password']:
			raise forms.ValidationError("The two passwords you typed do not match.")
		if len(self.data['password']) < 8:
			raise forms.ValidationError("Please enter a password that is at least 8 characters long.")
		return self.data['password']

	def clean_email(self):
		email = self.data['email']








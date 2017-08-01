import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms
MALE=0
FEMALE=1
CHOICES_GENDER=(
	(MALE,'MALE'),
	(FEMALE,'FEMALE'),
)

class UserForm(forms.Form):
	username=forms.CharField(label='ID', max_length=30, required=True)	
	password1=forms.CharField(label='Password',widget=forms.PasswordInput(),max_length=30,required=True)
	password2=forms.CharField(label='Confirm password',widget=forms.PasswordInput(),max_length=30,required=True)
	type=forms.CharField(label='type',default='G')
	birth=forms.DateField(label='date of birth')
	last_name=forms.CharField(label='lastname',max_length=10,)
	first_name=forms.CharField(label='firstname',max_length=10,)
	email=forms.EmailField(label='e-mail')
	phone=forms.CharField(label='phone',max_length=25,)
	gender=forms.ChoiceField(label='gender',choices=CHOICES_GENDER,widget=forms.RadioSelect())
	def is_valid_password(self):
		if 'password1' in self.cleaned_data:
			password1=self.cleaned_data['password1']
			password2=self.cleaned_data['password2']
			if password1==password2:
				return password2
			raise forms.ValidationError('password is not correct.')
	def is_valid_username(self):
		username=self.cleaned_data['username']
		username=username.lstrip().rstrip()
		if not re.search(r'^w+$',username):
			raise forms.ValidationError('username consists of alphabat, number and _')
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('already exists')

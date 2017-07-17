from django.db import models

# Create your models here.

class user(models.Model):
	id=models.CharField(max_length=20,primary_key=True,)	
	password=models.CharField(max_length=50,)
	email=models.EmailField(max_length=40,)
	phone=models.CharField(max_length=25,)
	gender=models.CharField(max_length=5,)
	type=models.CharField(max_length=5,default='G')
	birth=models.CharField(max_length=10,)
	

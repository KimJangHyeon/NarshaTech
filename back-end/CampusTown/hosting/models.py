from django.db import models
from login.forms import UserForm
from django.contrib.auth.models import User

# Create your models here.
class Host(models.Model) :
    id = models.ForeignKey(User, primary_key = True)
    picture = models.URLField()
    university = models.CharField(max_length = 50)
    location = models.CharField(max_length = 175)
    introduction = models.CharField(max_length = 500)
    universityIntroduction = models.CharField(max_length = 500)
    totalRating = models.FloatField()

from django.db import models
from login.forms import UserForm
from django.contrib.auth.models import User

# Create your models here.
class Host(models.Model) :
    user_id = models.ForeignKey(User, primary_key=True)
    picture = models.URLField(null=True, blank = True)
    university = models.CharField(max_length = 50, blank = True, null=True)
    location = models.CharField(max_length = 175, blank = True, null=True)
    introduction = models.CharField(max_length = 500, blank = True, null=True)
    universityIntroduction = models.CharField(max_length = 500, blank = True, null=True)
    totalRating = models.FloatField(default = 0.00)

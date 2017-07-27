from django.db import models
from .forms import UserForm

# Create your models here.
class Host(models.Model) :
    id = models.ForeignField(UserForm)
    picture = models.URLField()
    university = models.CharField(max_length = 50)
    location = models.CharField(max_length = 175)
    introduction = models.CharField(max_length = 500)
    universityIntroduction = models.CharField(max_length = 500)
    totalRating = models.FloatField()

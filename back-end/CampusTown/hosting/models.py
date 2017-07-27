from django.db import models
from .forms import UserForm

# Create your models here.
class Host(models.Model) :
    id = Model.ForeignField(UserForm)
    picture = Model.URLField()
    university = Model.CharField(max_length = 50)
    location = Model.CharField(max_length = 175)
    introduction = Model.CharField(max_length = 500)
    universityIntroduction = Model.CharField(max_length = 500)
    totalRating = Model.FloatField()

from django.db import models
from login import UserForm

# Create your models here.
class Host(models.Model) :
    id = Model.ForeignField(UserForm)
    picture = Model.CharField(max_length = 200, )
    university = Model.CharField(max_length = 50)
    location = Model.CharField(max_length = 175)
    introduction = Model.CharField(max_length = 500)
    universityIntroduction = Model.CharField(max_length = 500)
    totalRating = Model.FloatField()

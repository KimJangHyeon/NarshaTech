from django.db import models

# Create your models here.
class Main(models.Model) :
    image = models.CharField(max_length = 128)
    text = models.CharField(max_length = 500)
    title = models.CharField(max_length = 200)
    rating = models.FloatField(default = 0.00)

class Slide(models.Model) :
    image = models.CharField(max_length = 128)
    title = models.CharField(max_length = 200)

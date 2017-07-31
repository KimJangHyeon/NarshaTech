from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model) :
    user_id = models.ForeignKey(User)
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 20)
    activityLocation = models.CharField(max_length = 50)
    activityIntroduction = models.CharField(max_length = 500)
    vehicle = models.CharField(max_length = 30)
    meetingPlace = models.CharField(max_length = 128)
    price = models.FloatField()
    maximumCapacity = models.IntegerField()
    additionalInformation = models.CharField(max_length = 500)
    readyTime = models.FloatField()
    lastReadyTime = models.FloatField() #준비시간. 이때까지 예약인원이 0명인 경우 여행 계획 취소
    activityRating = models.FloatField() #막바지시간. 준비시간에 1명이라도 있었던 경우 다른 사람을 받을 수 있는 마지막 시간.
    totalTime = models.FloatField()

class ActivityLanguage(models.Model) :
    activityIndex = models.ForeignKey(Activity)
    language = models.CharField(max_length = 30)

class ActivitySchedule(models.Model) :
    activityIndex = models.ForeignKey(Activity)
    location = models.CharField(max_length = 128)
    startYear = models.IntegerField()
    startMonth = models.IntegerField()
    startHour = models.IntegerField()
    startMinute = models.IntegerField()
    endYear = models.IntegerField()
    endMonth = models.IntegerField()
    endDay = models.IntegerField()
    endHour = models.IntegerField()
    endMinute = models.IntegerField()
    url = models.URLField()
    introduction = models.CharField(max_length = 500)

class ActivityPicture(models.Model) :
    activityIndex = models.ForeignKey(Activity)
    url = models.URLField()

class HashTag(models.Model) :
    user_id = models.ForeignKey(User)
    hash = models.CharField(max_length = 20)
    activityIndex = models.ForeignKey(Activity)

class ActivityReview(models.Model) :
    activityIndex = models.ForeignKey(Activity)
    user_id = models.ForeignKey(User)
    review = models.CharField(max_length = 300)
    date = models.DateTimeField()
    rating = models.FloatField(default = 0.00)

class BookMark(models.Model) :
    user_id = models.ForeignKey(User)
    activityIndex = models.ForeignKey(Activity)

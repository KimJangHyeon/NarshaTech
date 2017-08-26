# -*- coding: utf-8 -*-

# new version
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
	
LANGUAGE=(
	('Korean','Korean'),
	('English','English'),
	('Japanese','Japanese'),
	('Chinese','Chinese'),
)

CATEGORIES=(
	('art/design','art/design'),
	('fashion','fashion'),
	('entertainment','entertainment'),
	('sports','sports'),
	('campustour','campustour'),
	('well-being','well-being'),
	('nature','nature'),
	('food','food'),
	('life style','life style'),
	('history','history'),
	('music','music'),
	('business','business'),
	('bar/club','bar/club'),
)
	

class ActivityInfo(models.Model) :
    user_id = models.ForeignKey(User,null=True, blank=True)
    title = models.CharField(max_length = 100,null=True, blank=True) 
    category = models.CharField(max_length = 30,choices=CATEGORIES,default='art/design')
    language=models.CharField(max_length=30, choices=LANGUAGE,default='Korean') 
    activityLocation = models.CharField(max_length = 50,null=True, blank=True) 
    activityIntroduction = models.CharField(max_length = 500,null=True, blank=True) 
    vehicle = models.CharField(max_length = 30,null=True, blank=True) 
    meetingPlace = models.CharField(max_length = 128,null=True, blank=True) 
    price = models.FloatField(default=0.0,null=True, blank=True) 
    maximumCapacity = models.IntegerField(default=0,null=True, blank=True) 
    additionalInformation = models.CharField(max_length = 500,null=True, blank=True) 
    readyTime = models.FloatField(default=0.0,null=True, blank=True) 
    lastReadyTime = models.FloatField(default=0.0,null=True, blank=True) #준비시간. 이때까지 예약인원이 0명인 경우 여행 계획 취소 
    activityRating = models.FloatField(default=0.0,null=True, blank=True) #막바지시간. 준비시간에 1명이라도 있었던 경우 다른 사람을 받을 수 있는 마지막 시간. 
    totalTime = models.FloatField(default=0.0,null=True, blank=True) 

#class ActivityLanguage(models.Model) :
 #   activityIndex = models.ForeignKey(ActivityInfo) 
  #  language = models.CharField(max_length = 30,choices=LANGUAGE,default='Korean') 

class ActivitySchedule(models.Model) :
    activityIndex = models.ForeignKey(ActivityInfo)
    location = models.CharField(max_length = 128) 
    startYear = models.IntegerField(default=0)
    startMonth = models.IntegerField(default=0) 
    startHour = models.IntegerField(default=0) 
    startMinute = models.IntegerField(default=0) 
    endYear = models.IntegerField(default=0) 
    endMonth = models.IntegerField(default=0) 
    endDay = models.IntegerField(default=0) 
    endHour = models.IntegerField(default=0) 
    endMinute = models.IntegerField(default=0) 
    url = models.URLField(null=True, blank=True) 
    introduction = models.CharField(max_length = 500,null=True, blank=True) 

class ActivityPicture(models.Model) :
    activityIndex = models.ForeignKey(ActivityInfo)
    url = models.URLField()

class HashTag(models.Model) :
    user_id = models.ForeignKey(User)
    hash = models.CharField(max_length = 20)
    activityIndex = models.ForeignKey(ActivityInfo)

class ActivityReview(models.Model) :
    activityIndex = models.ForeignKey(ActivityInfo)
    user_id = models.ForeignKey(User)
    review = models.CharField(max_length = 300) 
    date = models.DateTimeField() 
    rating = models.FloatField(default = 0.00) 

class BookMark(models.Model) :
    user_id = models.ForeignKey(User)
    activityIndex = models.ForeignKey(ActivityInfo)

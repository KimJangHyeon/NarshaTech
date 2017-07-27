from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model) :
    index = models.AutoField()
    id = models.ForeignKey(User)
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 20)
    activityDestination = models.CharField(max_length = 50)
    activityIntroduction = models.CharField(max_length = 500)
    meetingPlace = models.CharField(max_length = 128)
    price = models.FloatField()
    maximumCapacity = models.IntegerField()
    additionalInformation = models.CharField(max_length = 500)
    readyTime = models.FloatField()
    lastReadyTime = models.FloatField() #준비시간. 이때까지 예약인원이 0명인 경우 여행 계획 취소
    activityRating = models.FloatField() #막바지시간. 준비시간에 1명이라도 있었던 경우 다른 사람을 받을 수 있는 마지막 시간.
    totalHour = models.FloatField()

class ActivityLanguage(models.Model) :
    index = models.AutoField()
    activityIndex = models.ForeignKey(Activity)
    language = models.CharField(max_length = 30)

class ActivitySchedule(models.Model) :
    index = models.AutoField()
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
    index = models.AutoField()
    activityIndex = models.ForeignKey(Activity)
    url = models.URLField()

class HashTag(models.Model) :
    id = models.AutoField()
    hash = models.CharField(max_length = 20)
    activityIndex = models.ForeignField(Activity)

class ActivityReview(models.Model) :
    index = models.AutoField()
    activityIndex = models.ForeignField(Activity)
    id = models.ForeignField(User)
    review = models.CharField(max_length = 300)
    date = models.DateTimeField()
    rating = models.FloatField(default = 0.00)

"""
CREATE TABLE activity (
index INTEGER NOT NULL AUTO_INCREMENT,
id VARCHAR(20) NOT NULL,
title VARCHAR(100) NULL,
category VARCHAR(20) NOT NULL,
travelDestination VARCHAR(50) NOT NULL,
travelIntroduction VARCHAR(500) NOT NULL,
meetingPlace VARCHAR(128) NOT NULL,
price FLOAT(2) NOT NULL,
maximumCapacity INTEGER NOT NULL DEFAULT 1, --0 이하면 값 재설정.
additionalInformation VARCHAR(500) NULL DEFAULT NULL,
readyTime FLOAT(2) NOT NULL DEFAULT 0.00, --준비시간. 이때까지 예약인원이 0명인 경우 여행 아예 취소
lastReadyTime FLOAT(2) NOT NULL DEFAULT 0.00, --막바지시간. 준비시간에 예약인원이 1명이라도 있었던 경우 다른 사람을 받을 수 있는 마지막 시간.
activityRating FLOAT(2) NOT NULL DEFAULT 0.00,
totalHour FLOAT(2) NOT NULL, --여행 총 시간
PRIMARY KEY (index)
) COMMENT '여행의 개요를 담는 테이블입니다';

CREATE TABLE activityLanguage (
index INTEGER NOT NULL AUTO_INCREMENT,
activityIndex INTEGER NOT NULL ,
language VARCHAR(30) NOT NULL,
PRIMARY KEY (index)
) COMMENT 'activity에서 제공하는 언어를 저장하는 테이블';

CREATE TABLE activitySchedule (
index INTEGER NOT NULL AUTO_INCREMENT,
activityIndex INTEGER NOT NULL,
location VARCHAR(128) NOT NULL,
startYear INT NOT NULL,
startMonth INTEGER NOT NULL,
startDay INTEGER NOT NULL,
startHour INTEGER NOT NULL,
startMinute INTEGER NOT NULL,
endYear INTEGER NOT NULL,
endMonth INTEGER NOT NULL ,
endDay INTEGER NOT NULL,
endHour INTEGER NOT NULL,
endMinute INTEGER NOT NULL,
url VARCHAR(128) NULL,
introduction VARCHAR(500) NOT NULL,
PRIMARY KEY (index)
) COMMENT 'activity의 세부 정보를 저장하는 테이블';

DROP TABLE IF EXISTS activityPicture;

CREATE TABLE activityPicture ( --main picture을 담는 테이블.
index INTEGER NOT NULL AUTO_INCREMENT,
activityIndex INTEGER NOT NULL,
url VARCHAR(128) NOT NULL, --main picture
PRIMARY KEY (index)
) COMMENT '트립의 사진들을 저장하는 테이블';

DROP TABLE IF EXISTS hashTag;

CREATE TABLE hashTag ( --한 단어씩 받아와야함.
id INTEGER NOT NULL AUTO_INCREMENT,
hash VARCHAR(20) NOT NULL,
activityIndex INTEGER NOT NULL,
PRIMARY KEY (id)
) COMMENT 'activity의 해쉬태그를 저장하는 테이블';

DROP TABLE IF EXISTS activityReview;

CREATE TABLE activityReview (
index INTEGER NOT NULL AUTO_INCREMENT,
activityIndex INTEGER NOT NULL,
id VARCHAR(20) NOT NULL,
review VARCHAR(300) NOT NULL,
date DATETIME NULL,
rating FLOAT(2) NOT NULL DEFAULT 0.00,
PRIMARY KEY (index)
) COMMENT 'activity의 후기를 저장하는 테이블';
"""

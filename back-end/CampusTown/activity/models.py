from django.db import models
from login.forms import UserForm as User

# Create your models here.

class Activity(models.Model) :
    index = Model.AutoField()
    id = Model.ForeignField(User)
    title = Model.CharField(max_length = 100)
    category = Model.CharField(max_length = 20)
    travelDestination = Model.CharField(max_length = 50)
    travelIntroduction = Model.CharField(max_length = 500)
    meetingPlace = Model.CharField(max_length = 128)
    price = Model.FloatField()
    maximumCapacity = Model.InteterField()
    additionalInformation = Model.CharField(max_length = 500)
    readyTime = Model.FloatField()
    lastReadyTime = Model.FloatField() #준비시간. 이때까지 예약인원이 0명인 경우 여행 계획 취소
    activityRating = Model.FloatField() #막바지시간. 준비시간에 1명이라도 있었던 경우 다른 사람을 받을 수 있는 마지막 시간.
    totalHour = Model.FloatField()

class ActivityLanguage(models.Model) :
    index = Model.AutoField()
    activityIndex = Model.ForeignField(Activity)
    language = Model.CharField(max_length = 30)

class ActivitySchedule(models.Model) :
    index = Model.AutoField()
    activityIndex = Model.ForeignField(Activity)
    location = Model.CharField(max_length = 128)
    startYear = Model.InteterField()
    startMonth = Model.InteterField()
    startHour = Model.InteterField()
    startMinute = Model.InteterField()
    endYear = Model.InteterField()
    endMonth = Model.InteterField()
    endDay = Model.InteterField()
    endHour = Model.InteterField()
    endMinute = Model.InteterField()
    url = Model.URLField()
    introduction = Model.CharField(max_length = 500)

class ActivityPicture(models.Model) :
    index = Model.AutoField()
    activityIndex = Model.ForeignField(Activity)
    url = Model.URLField()

class HashTag(models.Model) :
    id = Model.AutoField()
    hash = Model.CharField(max_length = 20)
    activityIndex = Model.ForeignField(Activity)

class ActivityReview(models.Model) :
    index = Model.AutoField()
    activityIndex = Model.ForeignField(Activity)
    id = Model.ForeignField(User)
    review = Model.CharField(max_length = 300)
    date = Model.DateTimeField()
    rating = Model.FloatField(default = 0.00)

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

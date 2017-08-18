from django import forms
from .models import ActivityInfo, ActivitySchedule, ActivityPicture, HashTag, ActivityReview, Host #, ActivityLanguage
from django.contrib.auth.models import User

class ActivityDetail(forms.ModelForm) :
    class Meta :
        model = ActivityInfo
        fields = ["title", "category", "gatheringityLocation", "activityIntroduction", "vehicle", "meetingPlace", "price", "maximumCapacity", "additionalInformation", "readyTime", "lastReadyTime", "activityRating", "totalTime"]

class ActivityDetailPicture(forms.ModelForm) :
    class Meta :
        model = ActivityPicture
        fields = ["url"]

class ActivityDetailSchedule(forms.ModelForm) :
    class Meta :
        model = ActivitySchedule
        fields = ["location", "url", "introduction"]

class ActivityDetailHashTag(forms.ModelForm) :
    class Meta :
        model = HashTag
        fields = ["url"]

class ActivityDetailReview(forms.ModelForm) :
    class Meta :
        model = ActivityReview
        fields = ["user_id", "review", "date", "rating"]

class HostForm(forms.ModelForm) :
    class Meta :
        model = Host
        fields = ["picture", "university", "location", "introduction", "universityIntroduction", "totalRating"]

class UserForm(forms.ModelForm) :
    class Meta :
        model = User
        fields = ["last_name", "first_name", "gender"]

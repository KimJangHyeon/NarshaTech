from django import forms
from activity.models import ActivityInfo, ActivitySchedule, ActivityPicture, HashTag, ActivityReview #, ActivityLanguage
from hosting.models import Host
from django.contrib.auth.models import User

class ActivityDetail(forms.ModelForm) :
    class Meta :
        model = ActivityInfo
        fields = ["title", "category", "gatheringLocation", "activityIntroduction", "vehicle", "meetingPlace", "price", "maximumCapacity", "additionalInformation", "readyTime", "lastReadyTime", "activityRating", "totalTime"]

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
        moaZdel = HashTag
        fields = ["hash"]

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
        fields = ["last_name", "first_name"]

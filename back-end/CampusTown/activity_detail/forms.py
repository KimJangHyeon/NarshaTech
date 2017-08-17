from django import forms
from .models import ActivityInfo, ActivitySchedule, ActivityPicture, HashTag, ActivityReview, Host #, ActivityLanguage

class ActivityDetail(forms.ModelForm) :
    class Meta :
        model = ActivityInfo
        fields = []

class ActivityDetailPicture(forms.ModelForm) :
    class Meta :
        model = ActivityPicture
        fields = []

class ActivityDetailSchedule(forms.ModelForm) :
    class Meta :
        model = ActivitySchedule
        fields = []

class ActivityDetailHashTag(forms.ModelForm) :
    class Meta :
        model = HashTag
        fields = []

class ActivityDetailReview(forms.ModelForm) :
    class Meta :
        model = ActivityReview
        fields = []

class HostForm(forms.ModelForm) :
    class Meta :
        model = Host
        fields = []

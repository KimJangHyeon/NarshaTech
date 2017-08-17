from django import forms
from .models import Activity, ActivitySchedule, ActivityLanguage, ActivityPicture, HashTag, ActivityReview, BookMark

class Host4AcivityForm(forms.ModelForm) :
    class Meta :
        model = Activity
        fields = ('title', 'totalTime',)

class Host4HashTagForm(forms.ModelForm) :
    class Meta :
        model = HashTag
        fields = ('hash', )

class Host4ActivityPicture(forms.ModelForm) :
    class Meta :
        model = ActivityPicture
        fields = ('url', )

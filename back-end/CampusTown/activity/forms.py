from django import forms
from .models import ActivityInfo, ActivitySchedule, ActivityPicture, HashTag, ActivityReview, BookMark #ActivityLanguage

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
    ('well-being','well-being'),
    ('nature','nature'),
    ('food','food'),
    ('life style','life style'),
    ('history','history'),
    ('music','music'),
    ('business','business'),
    ('bar/club','bar/club'),
)

class ActivityForm(forms.ModelForm):
    category=forms.ChoiceField(choices=CATEGORIES, required=True)
    language=forms.ChoiceField(choices=LANGUAGE, required=True)
    class Meta:
        model=ActivityInfo  
        fields=('category','language',)


class Host4AcivityForm(forms.ModelForm) :
    class Meta :
        model = ActivityInfo
        fields = ('title', 'totalTime',)

class Host4HashTagForm(forms.ModelForm) :
    class Meta :
        model = HashTag
        fields = ('hash', )

class Host4ActivityPicture(forms.ModelForm) :
    class Meta :
        model = ActivityPicture
        fields = ('url', )

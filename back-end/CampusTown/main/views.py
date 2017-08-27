from django.shortcuts import render
from activity.models import ActivityInfo, ActivitySchedule, ActivityPicture, HashTag, ActivityReview #, ActivityLanguage

# Create your views here.
def content_list(request):
    contents = ActivityInfo.objects.all();
    pictures = ActivityPicture.objects.all();
    return render(request, 'main/content.html', {'contents' : contents, 'pictures' : pictures})

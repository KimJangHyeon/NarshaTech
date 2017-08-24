from django.shortcuts import render
from activity.models import Activity, ActivitySchedule, ActivityPicture, HashTag, ActivityReview #, ActivityLanguage

# Create your views here.
def content_list(request):
    contents = Activity.objects.all();
    pictures = ActivityPicture.objects.all();
    return render(request, 'main/content.html', {'contents' : contents, 'pictures' : pictures})

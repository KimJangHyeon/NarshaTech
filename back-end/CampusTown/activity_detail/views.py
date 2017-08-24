from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from activity.models import Activity, ActivitySchedule, ActivityPicture, HashTag, ActivityReview #, ActivityLanguage
from hosting.models import Host
from .forms import ActivityDetail, ActivityDetailPicture, ActivityDetailHashTag, ActivityDetailReview, HostForm, UserForm, ActivityDetailSchedule

# Create your views here.
def detail(request, pk) :
    activity = get_object_or_404(Activity, pk=pk)
    picture = ActivityPicture.objects.filter(activityIndex=pk)
    schedule = ActivitySchedule.objects.filter(activityIndex=pk)
    hash_tag = HashTag.objects.filter(activityIndex=pk)
    review = ActivityReview.objects.filter(activityIndex=pk)
    host = get_object_or_404(Host, user_id = activity.user_id)
    context = { "detail" : activity, "picture" : picture, "hashtags" : hash_tag, "reviews" : review, "host" : host, "schedules" : schedule}
    return render(request, 'activity_detail/activity_detail.html', context)

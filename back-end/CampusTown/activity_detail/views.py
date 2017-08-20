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
    review = ActivityReview.objects.filter(ActivityReview=pk)
    host = get_object_or_404(Host, id = user_id)
    user = get_object_or_404(User, username = user_id)
    context = { "detail" : activity, "picture" : picture, "hash_tag" : hash_tag, "review" : review, "user" : user, "host" : host, "schedule" : schedule, "reviewer" : reviewer}
    return render(request, 'activity_detail/activity_detail.html', context)

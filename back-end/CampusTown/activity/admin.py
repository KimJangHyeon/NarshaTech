from django.contrib import admin
from .models import ActivityInfo, ActivitySchedule, ActivityPicture, HashTag, ActivityReview, BookMark

# Register your models here.
admin.site.register(ActivityInfo)
admin.site.register(ActivitySchedule)
admin.site.register(ActivityPicture)
admin.site.register(HashTag)
admin.site.register(ActivityReview)
from django.shortcuts import render

# Create your views here.
def detail(request) :
    context = {}
    return render(request, 'activity_detail/activity_detail.html',context)

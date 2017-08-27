from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader, Context
from django.http import HttpResponse
from .models import ActivityInfo
from .forms import ActivityForm, Host4AcivityForm, Host4ActivityPicture, Host4HashTagForm

# Create your views here.
def host(request) :
    return render(request, 'activity/startHosting.html', {})

def host0(request) :
    return render(request, 'activity/host0.html', {})

def host1(request):
    return render(request,'activity/host1.html',{})

def host2(request):
    if request.method=="POST":
        form=ActivityForm(request.POST)
        if form.is_valid():
            new_activity=form.save(commit=False)
            new_activity.save()
            return redirect('host4', pk=new_activity.pk)
    else:
        form=ActivityForm()
    return render(request,'activity/host2.html',{'form':form})

def host3(request) : #guide auth
    page_title = 'host4'
    tpl = loader.get_template('host4.html')
    ctx = context({
        'page_title':page_title
    })
    return HttpResponse(tpl.render(ctx))

def host4(request, pk) :
    activity = get_object_or_404(ActivityInfo, pk=pk)
    if request.method=="POST" :
        #needed forms : Host4AcivityForm Host4HashTagForm Host4ActivityPicture
        form = Host4AcivityForm(request.POST, instance=activity)
        hash_tag = Host4HashTagForm(request.POST)
        pictures = Host4ActivityPicture(request.POST)
        if form.is_valid() :
            #form save
            activity = form.save(commit = False)
            new_hash = hash_tag.save(commit = False)
            new_picture = pictures.save(commit = False)
            activity.save()
            new_hash.save()
            new_picture.save()
            return redirect('host5', pk=activity.pk)
    else :
        #needed forms
        form = Host4AcivityForm(instance = activity)
        hash_tag = Host4HashTagForm()
        pictures = Host4ActivityPicture()
    return render(request, 'activity/host4.html', {'activity' : activity, 'hash_tag' : hash_tag, 'pictures' : pictures})
"""
def host4(request) :
    if request.method=="POST" :
        #needed forms : Host4AcivityForm Host4HashTagForm Host4ActivityPicture
        form = Host4AcivityForm(request.POST)
        hash_tag = Host4HashTagForm(request.POST)
        pictures = Host4ActivityPicture(request.POST)
        if form.is_valid() :
            #form save
            activity = form.save(commit = False)
            new_hash = hash_tag.save(commit = False)
            new_picture = pictures.save(commit = False)
            activity.save()
            new_hash.save()
            new_picture.save()
            return redirect('host5', pk=activity.pk)
    else :
        #needed forms
        form = Host4AcivityForm()
        hash_tag = Host4HashTagForm()
        pictures = Host4ActivityPicture()
    return render(request, 'activity/host4.html', {'activity' : form, 'hash_tag' : hash_tag, 'pictures' : pictures})
"""
def host5(request, pk) :
    page_title = 'host4'
    tpl = loader.get_template('activity/host4.html')
    ctx = {
        'page_title':page_title
    }
    return HttpResponse(tpl.render(ctx))

def host6(request) :
    page_title = 'host4'
    tpl = loader.get_template('host4.html')
    ctx = context({
        'page_title':page_title
    })
    return HttpResponse(tpl.render(ctx))

def host7(request) :
    page_title = 'host4'
    tpl = loader.get_template('host4.html')
    ctx = context({
        'page_title':page_title
    })
    return HttpResponse(tpl.render(ctx))

def host8(request,pk):
    activity=get_object_or_404(ActivityInfo,pk=pk)
    context={"new_activity":activity}
    return render(request,'activity/host8.html',context)

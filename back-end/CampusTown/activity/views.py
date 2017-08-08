from django.shortcuts import render, redirect
from django.template import loader, Context
from django.http import HttpResponse

# Create your views here.
def host0(request) :
    page_title = 'host4'
    tpl = loader.get_template('host4.html')
    ctx = context({
        'page_title':page_title
    })
    return HttpResponse(tpl.render(ctx))

def host1(request) :
    page_title = 'host4'
    tpl = loader.get_template('host4.html')
    ctx = context({
        'page_title':page_title
    })
    return HttpResponse(tpl.render(ctx))

def host2(request) :
    page_title = 'host4'
    tpl = loader.get_template('host4.html')
    ctx = context({
        'page_title':page_title
    })
    return HttpResponse(tpl.render(ctx))

def host3(request) :
    page_title = 'host4'
    tpl = loader.get_template('host4.html')
    ctx = context({
        'page_title':page_title
    })
    return HttpResponse(tpl.render(ctx))

def host4(request) :
    page_title = 'host4'
    ctx = {
        'page_title':page_title
    }
    tpl = loader.render_to_string('activity/host4.html', ctx)
    return HttpResponse(tpl)

def add_host4(request) :
    key = request.data.dict()
    if 'htitle' in key == False :
        return HttpResponse('input title')

    #if request.POST.has_key('htitle') == False :
    #    return HttpResponse('input title')
    else:
        #아직 글자수 처리 안함.
        title = request.POST('title')
    #if request.POST.has_key('htag') == False :
    if 'htag' in key == False :
        return HttpResponse('input tag')
    else:
        tag = request.POST['htag']
    #if request.POST.has_key('imgload') == True :
    #    picture = imgload
    ##totalTime // htrip_start & htrip_end
    return HttpDirect("/activity/5/")

def host5(request) :
    page_title = 'host4'
    tpl = loader.get_template('host4.html')
    ctx = context({
        'page_title':page_title
    })
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

def host8(request) :
    page_title = 'host4'
    tpl = loader.get_template('host4.html')
    ctx = context({
        'page_title':page_title
    })
    return HttpResponse(tpl.render(ctx))

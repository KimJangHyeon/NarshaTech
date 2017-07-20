from django.shortcuts import render
from .models import Main

# Create your views here.
def content_list(request):
    contents = Main.objects.all()
    return render(request, 'main/content.html', {'contents' : contents})

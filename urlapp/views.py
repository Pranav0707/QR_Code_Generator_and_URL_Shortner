import io
from django.http import HttpResponse
from django.shortcuts import render
import uuid
import pyshorteners
from qrcode import *
from urlapp.models import UrlShortner
from PIL import Image
from django.conf import settings
# Create your views here.
def index(request):
    pass

def shorten_url(request):
    if request.method=="POST":
        link=request.POST.get('url')
        py=pyshorteners.Shortener()
        short_url=py.tinyurl.short(link)
        image=make(link)
        url_model=UrlShortner(link=link,short_url=short_url)
        url_model.save()
        
    table_data=UrlShortner.objects.all()
    context={
        'table_data':table_data
    }
    return render(request,"urlapp/base.html",context)
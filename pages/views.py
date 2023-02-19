from django.shortcuts import render, HttpResponse
from .models import SiteInfo

# Create your views here.
def home_view(request):
    data = SiteInfo.objects.all()
    context = {}
    if data:
        context = {"data" : data[0]}
        
    #print(data[0].email)
    #print(data[0].subtitle) ki irhatjuk za adatbazisból a z infokat
    #print(data[0].name)

    return render(request, "home.html", context)

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request, "contact.html")

def gallery_view(request):
    return render(request, "gallery.html")

#2.43 
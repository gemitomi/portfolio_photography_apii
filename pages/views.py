from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(request):
    context = {
        "name": "Tom Tom",
        "subtitle": "photo"
    }
    return render(request, "home.html", context)

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request, "contact.html")

def gallery_view(request):
    return render(request, "gallery.html")
    
from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(request):
    return render(request, "home.html")

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request, "contact.html")
    
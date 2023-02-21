from django.urls import path
from .views import HomeView, SiteInfoView



urlpatterns = [
    path("", HomeView.as_view()),
    path("siteinfo/", SiteInfoView.as_view()),
]
# path("", home_view),
  #  path("about/", about_view),
   # path("contact/", contact_view),   
  #  path("gallery/", gallery_view),   
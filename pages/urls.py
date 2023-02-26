from django.urls import path
# from .views import HomeView, SiteInfoView
from .views import SiteInfoView, AboutView, CategoryView, GalleryView


urlpatterns = [
    path("siteinfo/", SiteInfoView.as_view()),
    path("about/", AboutView.as_view()),
    path("categories/", CategoryView.as_view()),
    path("gallery/", GalleryView.as_view())
]
# path("", home_view),
  #  path("about/", about_view),
   # path("contact/", contact_view),   
  #  path("gallery/", gallery_view),   
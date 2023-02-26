from django.contrib import admin

from .models import SiteInfo, About, Categories, Photo, LandingPage

admin.site.register(SiteInfo)
admin.site.register(About)
admin.site.register(Categories)
admin.site.register(LandingPage)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ["image", "category"]
    search_fields = ["image"]
    list_filter = ["category"]

admin.site.register(Photo, PhotoAdmin)



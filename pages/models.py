from django.db import models

class SiteInfo(models.Model):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"

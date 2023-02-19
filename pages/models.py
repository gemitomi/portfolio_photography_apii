from django.db import models 
from django.core.validators import FileExtensionValidator 

class SiteInfo(models.Model):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"



class About(models.Model):
    image = models.ImageField(
        upload_to="about",
        help_text="Select your profile picture. (.jpg)",
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])]
    )
    text = models.TextField(max_length=2000)

    def __str__(self) -> str:
        return self.text
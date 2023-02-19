from django.db import models 
from django.core.validators import FileExtensionValidator
from PIL import Image 

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # open image and resize
        image_path = self.image.path
        img = Image.open(image_path)
        max_size = 600

        if img.size[0] > max_size or img.size[1] > max_size:
            img.thumbnail((max_size, max_size))
            img.save(image_path)

    def __str__(self) -> str:
        return self.text
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.core.mail import send_mail
import random, time

from .models import SiteInfo, About, Categories, Photo, LandingPage

class SiteInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = SiteInfo.objects.all()
        if not data:
            return Response("This data is empty")

        return Response(
            {
                "name": data[0].name,
                "subtitle": data[0].subtitle,
                "email": data[0].email
            }
        )

class LandingPageView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = LandingPage.objects.all()
        if not data:
            return Response("No data for LandingPage")
        
        return Response(
            {
                "images": self.get_images(),
                "title": data[0].title,
                "slogen": data[0].slogen
            }
        )
    
    def get_images(self):
        photos = Photo.objects.all()
        if not photos:
            return []
        
        photo_list = [
            f"{self.request.build_absolute_uri('/')[:-1]}{i.image.url}" #azért kell a self mert a metodusba nem jön be a request
            for i in photos
        ]        
        random.shuffle(photo_list) # összekeveri a fotókat

        return photo_list[:6]

class AboutView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = About.objects.all()    # lehetne first()
        if not data:
            return Response("About is missing")

        return Response({
            "image" : f"{request.build_absolute_uri('/')[:-1]}{data[0].image.url}",
            "text" : data[0].text
        })

class CategoryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = Categories.objects.all()
        if not data:
            return Response("Categories are missing")  
        
        response_data = []
        for i in data:
            response_data.append(
                {
                    "id": i.id,
                    "name": i.name, 
                    "image": self.get_random_image_for_category(i.name)
                }
            )        
        return Response(response_data)

    def get_random_image_for_category(self, category):
        photos = Photo.objects.filter(category__name=category)
        random_image = random.choice(photos)
        return f"{self.request.build_absolute_uri('/')[:-1]}{random_image.image.url}"

class GalleryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = Photo.objects.all()
        if not data:
            return Response("No photo uploaded")
        
        response_data = []
        for i in data:
            response_data.append({
                "id": i.id,
                "category": i.category.name,
                "image": f"{self.request.build_absolute_uri('/')[:-1]}{i.image.url}"
            })

        return Response(response_data)

class ContactView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        post_data = request.data

        name = post_data.get("name")
        email = post_data.get("email")
        phone = post_data.get("phone")
        message = post_data.get("message")

        time.sleep(3)
        
        send_mail(
            f"Contact: {name}", # subject
            f"{message}\n\nPhone: {phone}",  # message
            email,  # mail from
            ["info@webrabbit.hu"], # mail to
            fail_silently=False
        )

        return Response("Ok", status.HTTP_202_ACCEPTED)




# class HomeView(APIView):
  #  permission_classes = [AllowAny]
   # def get(self, request):
    #    return Response(
     #           {
      #              "message": "Hello world"
       #         }
        #    )



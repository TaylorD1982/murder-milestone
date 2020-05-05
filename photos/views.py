from django.shortcuts import render
from .models import Photo

# Create your views here.
def all_photos(request):
    photos = Photo.objects.order_by('created_date')
    return render(request, "photos.html", {"photos": photos})

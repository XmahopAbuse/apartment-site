from django.http.response import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Appartment, AppartmentImage

def index(request):
    return render(request, "main_app/index.html")

def apartment_detail(request, url):
    try:
        apartment = Appartment.objects.get(url=url)
        images = AppartmentImage.objects.filter(appartment=apartment)
        main_image = images[0]
    except Appartment.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'main_app/apartment_detail.html', {'apartment': apartment, 'images': images, 'main_image':main_image})

def apartment_list(request):
    return HttpResponse(str("test"))
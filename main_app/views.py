from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Appartment, AppartmentImage
from django.views.decorators.csrf import csrf_exempt
from .forms import ApplicationForm
from django.http import JsonResponse
from django.core import serializers


def index(request):
    form = ApplicationForm()
    try:
        apartments = Appartment.objects.filter(show_in_main=True)[:3]
        for apartment in apartments:
            image = AppartmentImage.objects.filter(appartment=apartment)[:1]
            apartment.image = image

    except Appartment.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'main_app/index.html', {'apartments': apartments, 'form':form})

def apartment_detail(request, url):
    form = ApplicationForm()
    try:
        apartment = Appartment.objects.get(url=url)
        images = AppartmentImage.objects.filter(appartment=apartment)
    except Appartment.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'main_app/apartment_detail.html', {'apartment': apartment, 'images': images, 'form':form})

def apartment_list(request):
    try:
        apartments = Appartment.objects.all()
        for apartment in apartments:
            image = AppartmentImage.objects.filter(appartment=apartment)[:1]
            apartment.image = image

    except Appartment.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'main_app/apartments.html', {'apartments': apartments})

def contacts(request):
    return render(request, 'main_app/contacts.html')


def application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [ instance, ])
            return HttpResponse("test1")
        else:
            return HttpResponse("test2")
    return HttpResponse("test3")
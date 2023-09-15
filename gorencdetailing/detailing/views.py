from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Storitev, Priporočila, Termini, Galerija, Kontakt

def storitve_view(request):
    services = Storitev.objects.all()
    return render(request, 'storitve.html', {'services': services})

def priporocila_view(request):
    testimonials = Priporočila.objects.all()
    return render(request, 'priporocila.html', {'testimonials': testimonials})

def termini_view(request):
    termini = Termini.objects.all()
    return render(request, 'termini.html', {'termini': termini})

def galerija_view(request):
    galerija = Galerija.objects.all()
    return render(request, 'galerija_slik.html', {'galerija': galerija})

def kontakt_view(request):
    kontakt = Kontakt.objects.first()  
    return render(request, 'kontakt.html', {'kontakt': kontakt})

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Storitev, Priporočila, Termini, Galerija, Kontakt

def storitve_view(request):
    active_page = 'storitve'
    storitve = Storitev.objects.all()
    return render(request, 'storitve.html', {'active_page': active_page, 'storitve': storitve})

def priporocila_view(request):
    active_page = 'priporocila'
    priporocila = Priporočila.objects.all()
    return render(request, 'priporocila.html', {'active_page': active_page, 'priporocila': priporocila})

def termini_view(request):
    active_page = 'termini'
    termini = Termini.objects.all()
    return render(request, 'termini.html', {'active_page': active_page, 'termini': termini})

def galerija_view(request):
    active_page = 'galerija'
    galerija = Galerija.objects.all()
    return render(request, 'galerija_slik.html', {'active_page': active_page, 'galerija': galerija})

def kontakt_view(request):
    active_page = 'kontakt'
    kontakt = Kontakt.objects.first()  
    return render(request, 'kontakt.html', {'active_page': active_page, 'kontakt': kontakt})

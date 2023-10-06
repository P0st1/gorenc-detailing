from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Storitev, Priporočila, Termini, Kontakt, KontaktStranka, Avto, AvtoSlike
from .forms import KontaktObrazec
from itertools import groupby

def domaca_stran_view(request):
    return render(request, 'domaca_stran.html')

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

def avto_slideshow(request):
    avti = Avto.objects.prefetch_related('avtoslike_set')  
    return render(request, 'galerija_slik.html', {'avti': avti})



def kontakt_view(request):
    active_page = 'kontakt'
    kontakt = Kontakt.objects.first()  
    return render(request, 'kontakt.html', {'active_page': active_page, 'kontakt': kontakt})

def kontakt_obrazec_view(request):
    if request.method == 'POST':
        obrazec = KontaktObrazec(request.POST)
        if obrazec.is_valid():
            obrazec.save()
            messages.success(request, 'Vaš obrazec je bil uspešno poslan. Kontaktirali vas bomo v kratkem.')
            return redirect('domaca_stran')
    else:
        obrazec = KontaktObrazec()
    
    return render(request, 'kontakt_obrazec.html', {'obrazec': obrazec})

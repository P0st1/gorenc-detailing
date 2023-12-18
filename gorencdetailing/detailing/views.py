from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Storitev, Priporočila, Kontakt, KontaktStranka, Avto, AvtoSlike, CarLineSlike
from .forms import KontaktObrazec
from django.core.mail import send_mail

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


def avto_slideshow(request):
    avti = Avto.objects.prefetch_related('avtoslike_set')  
    car_line_slike = CarLineSlike.objects.all()
    return render(request, 'galerija_slik.html', {'avti': avti, 'car_line_slike': car_line_slike})



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
        obrazec = KontaktObrazec(initial={'ime': '', 'email': '', 'telefonska_stevilka': '', 'vas_avto': '', 'storitev': '', 'sporocilo': ''})
    
    return render(request, 'kontakt_obrazec.html', {'obrazec': obrazec})


def appointments_view(request):
    if request.method == "POST":
        ime = request.POST['ime']
        email = request.POST['email']
        telefon = request.POST['telefon']
        avto = request.POST['avto']
        sporocilo = request.POST['sporocilo']
        storitev = request.POST.getlist('storitev')

    #    # send an email
    #     send_mail(
    #         ime,
    #         email, 
    #         telefon,
    #         avto,
    #         sporocilo, 
    #         storitev,
    #     ['detailing.gorenc@gmail.com'], # na mail
    #       )
        return render(request, 'appointments.html', {
        'ime': ime,
        'email': email,
        'telefon': telefon,
        'avto': avto,
        'sporocilo': sporocilo, 
        'storitev': storitev,
                })

    else:
        return render(request, 'domaca_stran.html', {})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Storitev, Priporočila, Kontakt, KontaktStranka, Avto, AvtoSlike, CarLineSlike
from .forms import KontaktObrazec
from django.core.mail import send_mail
from django.db.models import Avg, Count
from django.conf import settings
from django.core.mail import send_mail


def domaca_stran_view(request):
    return render(request, 'domaca_stran.html')


def storitve_view(request):
    active_page = 'storitve'
    storitve = Storitev.objects.all()
    return render(request, 'storitve.html', {'active_page': active_page, 'storitve': storitve})


def priporocila_view(request):
    context={}
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        testimonial = request.POST.get('testimonial')
        rating = request.POST.get('rating')
        datum_storitve = request.POST.get('datum_storitve')
        type_of_service_id = request.POST.get('type_of_service')

        type_of_service = get_object_or_404(Storitev, id=type_of_service_id)

        new_priporocilo = Priporočila(
            user_name=user_name,
            testimonial=testimonial,
            rating=rating,
            datum_storitve=datum_storitve,
            type_of_service=type_of_service  
        )
        new_priporocilo.save()
        messages.success(request, 'Vaše mnenje je bilo uspešno poslano. Hvala!')
        return redirect('priporocila') 
    storitve = Storitev.objects.all()
    active_page = 'priporocila'
    priporocila = Priporočila.objects.all().order_by('?')
    # Calculate average rating
    avg_result = Priporočila.objects.aggregate(Avg('rating'))
    avg_rating = avg_result.get('rating__avg')

    # Handle None case
    if avg_rating is None:
        avg_rating = "No ratings"  # or any other default value or message
    else:
        avg_rating = f"{avg_rating:.2f}"
    testimonial_count = Priporočila.objects.count()

    context = {
        'active_page': active_page,
        'priporocila': priporocila,
        'storitve': storitve,
        'avg_rating': avg_rating,
        'testimonial_count': testimonial_count,
    }
    return render(request, 'priporocila.html', context)


def avto_slideshow(request):
    active_page = 'galerija'
    avti = Avto.objects.prefetch_related('avtoslike_set')  
    car_line_slike = CarLineSlike.objects.all()
    return render(request, 'galerija_slik.html', {'active_page': active_page, 'avti': avti, 'car_line_slike': car_line_slike})


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
    active_page = 'kontakt_obrazec'
    return render(request, 'kontakt_obrazec.html', {'obrazec': obrazec, 'active_page': active_page})


def narocila_view(request):
    if request.method == "POST":
        ime = request.POST['ime']
        email = request.POST['email']
        telefon = request.POST['telefon']
        avto = request.POST['avto']
        sporocilo = request.POST['sporocilo']
        storitev = request.POST.getlist('storitev')

        # Celo ime storitve namesto ID-ja v imenu
        storitev_ime = Storitev.objects.filter(id__in=storitev).values_list('naslov', flat=True)

        # Format the email message
        message = f"Ime in priimek: {ime}\nE-pošta: {email}\nTelefon: {telefon}\nAvto: {avto}\nStoritev: {', '.join(storitev_ime)}\nSporočilo: {sporocilo}"

        send_mail(
            subject="Nova stranka pošilja povpraševanje",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['detailing.gorenc@gmail.com'],
        )
        
        return render(request, 'narocila.html', {
            'ime': ime,
            'email': email,
            'telefon': telefon,
            'avto': avto,
            'sporocilo': sporocilo, 
            'storitev': storitev,
        })
    else:
        return render(request, 'domaca_stran.html', {})
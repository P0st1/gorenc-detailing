from django.db import models

class Storitev(models.Model):
    naslov = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=8, decimal_places=2)
    icon_class = models.CharField(max_length=50, help_text="Add the icon class for this service")

    def __str__(self):
        return self.naslov
    
class Priporočila(models.Model):
    user_name = models.CharField(max_length=100)
    testimonial = models.TextField()
    rating = models.IntegerField(default=5)
    datum_storitve = models.DateField(verbose_name='Datum storitve', null=True)
    type_of_service = models.ForeignKey(Storitev, on_delete=models.CASCADE, null=True, verbose_name='Vrsta storitve')

    def __str__(self):
        return f"Priporočilo od {self.user_name}"
    
class Avto(models.Model):
    znamka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    opis = models.TextField()
    
    def __str__(self):
        return f"{self.znamka} {self.model}"

class AvtoSlike(models.Model):
    avto = models.ForeignKey(Avto, on_delete=models.CASCADE) 
    slika = models.ImageField(upload_to='galerija_slik')
    
    def __str__(self):
        return self.slika.name

class CarLineSlike(models.Model):
    car_line_slika = models.ImageField()
    
class Kontakt(models.Model):
    ime_podjetja = models.CharField(max_length=100, default='Gorenc Detailing')
    naslov = models.CharField(max_length=200, default='Hrastno pri Šentrupertu 9')
    email = models.EmailField()
    telefon = models.CharField(max_length=15)
    google_maps_embed = models.TextField(default='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12345.12345!2d-74.12345!3d40.12345!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMjfCsDAwJzUwLjUiTiA3NMKwMzMnMjMuMyJX!5e0!3m2!1sen!2sus!4v1234567890!5m2!1sen!2sus"></iframe>')
    delovni_cas = models.CharField(max_length=200)

    def __str__(self):
        return self.ime_podjetja
    
class KontaktStranka(models.Model):
    ime = models.CharField(max_length=100)
    email = models.EmailField()
    telefonska_stevilka = models.CharField(max_length=15)
    vas_avto = models.CharField(max_length=100)
    sporocilo = models.TextField()
    storitev = models.ManyToManyField(Storitev)





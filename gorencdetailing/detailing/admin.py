from django.contrib import admin
from .models import Storitev, Priporočila, Kontakt, Avto, AvtoSlike, CarLineSlike

class AvtoSlikeInline(admin.TabularInline):
  model = AvtoSlike
  extra = 10

class AvtoAdmin(admin.ModelAdmin):
  inlines = [AvtoSlikeInline]





admin.site.register(Storitev)
admin.site.register(Priporočila)
admin.site.register(Kontakt)
admin.site.register(Avto)
admin.site.register(AvtoSlike)
admin.site.register(CarLineSlike)
from django.contrib import admin
from .models import Pizza, Sos, Kucharz, Kierowca, Klient, DodatkowySkladnik, Zamowienie

admin.site.register(Pizza)
admin.site.register(Sos)
admin.site.register(Kucharz)
admin.site.register(Kierowca)
admin.site.register(Klient)
admin.site.register(DodatkowySkladnik)
admin.site.register(Zamowienie)
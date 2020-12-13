from rest_framework import serializers
from .models import Klient, Pizza, Kucharz, Kierowca, Sos, Zamowienie

class KlientSerializer(serializers.ModelSerializer):
   class Meta:
       model = Klient
       fields = ['imie','nazwisko','telefon','adres']

class PizzaSerializer(serializers.ModelSerializer):
   class Meta:
       model = Pizza
       fields = ['nazwa','opis','cena']

class KucharzSerializer(serializers.ModelSerializer):
   class Meta:
       model = Kucharz
       fields = ['imie', 'nazwisko']
class KierowcaSerializer(serializers.ModelSerializer):
   class Meta:
       model = Kierowca
       fields = ['imie', 'nazwisko']
class SosSerializer(serializers.ModelSerializer):
   class Meta:
       model = Sos
       fields = ['nazwa', 'cena']

class ZamowienieSerializer(serializers.ModelSerializer):
   class Meta:
       model = Zamowienie
       fields = ['klient', 'kierowca', 'kucharz', 'pizza', 'cena_zamowienia', 'data_realizacji']
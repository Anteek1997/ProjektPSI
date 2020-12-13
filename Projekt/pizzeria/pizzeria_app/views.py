from django.shortcuts import render
from django.http import HttpResponse
from .models import Klient, Pizza, Kucharz, Kierowca, Sos, Zamowienie
from .serializers import KlientSerializer,PizzaSerializer, KucharzSerializer,KierowcaSerializer,SosSerializer, ZamowienieSerializer
from rest_framework import generics

def index(request):
    return HttpResponse("<h1>Witamy na stronie pizzeri!")

class KlientView(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer

class KlientDetails(generics.RetrieveDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer

class PizzaView(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class PizzaDetails(generics.RetrieveDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class KucharzView(generics.ListCreateAPIView):
    queryset = Kucharz.objects.all()
    serializer_class = KucharzSerializer

class KucharzDetails(generics.RetrieveDestroyAPIView):
    queryset = Kucharz.objects.all()
    serializer_class = KucharzSerializer

class KierowcaView(generics.ListCreateAPIView):
    queryset = Kierowca.objects.all()
    serializer_class = KierowcaSerializer

class KierowcaDetails(generics.RetrieveDestroyAPIView):
    queryset = Kierowca.objects.all()
    serializer_class = KierowcaSerializer

class SosView(generics.ListCreateAPIView):
    queryset = Sos.objects.all()
    serializer_class = SosSerializer

class SosDetails(generics.RetrieveDestroyAPIView):
    queryset = Sos.objects.all()
    serializer_class = SosSerializer

class ZamowienieView(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer

class ZamowienieDetails(generics.RetrieveDestroyAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
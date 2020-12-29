from django.shortcuts import render
from django.http import HttpResponse
from .models import Klient, Pizza, Kucharz, Kierowca, Sos, Zamowienie
from .serializers import KlientSerializer, PizzaSerializer, KucharzSerializer, KierowcaSerializer, SosSerializer, \
    ZamowienieSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse
from rest_framework.response import Response


def index(request):
    return HttpResponse("<h1>Witamy na stronie pizzeri!")


class KlientView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'client-list'


class KlientDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'client-detail'


class PizzaView(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    name = 'pizza-list'


class PizzaDetails(generics.RetrieveDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    name = 'pizza-detail'


class KucharzView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Kucharz.objects.all()
    serializer_class = KucharzSerializer
    name = 'chief-list'


class KucharzDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Kucharz.objects.all()
    serializer_class = KucharzSerializer
    name = 'chief-detail'


class KierowcaView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Kierowca.objects.all()
    serializer_class = KierowcaSerializer
    name = 'driver-list'


class KierowcaDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Kierowca.objects.all()
    serializer_class = KierowcaSerializer
    name = 'driver-detail'


class SosView(generics.ListCreateAPIView):
    queryset = Sos.objects.all()
    serializer_class = SosSerializer
    name = 'sauce-list'


class SosDetails(generics.RetrieveDestroyAPIView):
    queryset = Sos.objects.all()
    serializer_class = SosSerializer
    name = 'sauce-detail'


class ZamowienieView(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'order-list'


class ZamowienieDetails(generics.RetrieveDestroyAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'order-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'Client': reverse(KlientView.name, request=request),
                         'Sauce': reverse(SosView.name, request=request),
                         'Pizza': reverse(PizzaView.name, request=request),
                         'Driver': reverse(KierowcaView.name, request=request),
                         'Chief': reverse(KucharzView.name, request=request),
                         'Order': reverse(ZamowienieView.name, request=request)
                         })

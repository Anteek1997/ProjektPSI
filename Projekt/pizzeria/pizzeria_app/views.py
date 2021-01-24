from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza, Sauce, Chef, Driver, Client, Order_Restaurant, Order_Client
from .serializers import ClientSerializer, PizzaSerializer, ChefSerializer, DriverSerializer, SauceSerializer, \
    Order_ClientSerializer, Order_RestaurantSerializer, UserSerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser


def index(request):
    return HttpResponse("<h1>Witamy na stronie pizzeri!")


class ClientView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'
    filterset_fields = ['name', 'surname']
    search_fields = ['name', 'surname']
    ordering_fields = ['name', 'surname']


class ClientDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'
    filterset_fields = ['name', 'surname']
    search_fields = ['name', 'surname']
    ordering_fields = ['name', 'surname']


class PizzaView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    name = 'pizza-list'
    filterset_fields = ['name', 'price']
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'price']


class PizzaDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    name = 'pizza-detail'
    filterset_fields = ['name', 'price']
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'price']


class ChefView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
    name = 'chef-list'
    filterset_fields = ['name', 'surname']
    search_fields = ['name', 'surname']
    ordering_fields = ['name', 'surname']


class ChefDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
    name = 'chef-detail'
    filterset_fields = ['name', 'surname']
    search_fields = ['name', 'surname']
    ordering_fields = ['name', 'surname']


class DriverView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    name = 'driver-list'
    filterset_fields = ['name', 'surname']
    search_fields = ['name', 'surname']
    ordering_fields = ['name', 'surname']


class DriverDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    name = 'driver-detail'
    filterset_fields = ['name', 'surname']
    search_fields = ['name', 'surname']
    ordering_fields = ['name', 'surname']


class SauceView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Sauce.objects.all()
    serializer_class = SauceSerializer
    name = 'sauce-list'
    filterset_fields = ['name', 'price']
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'price']


class SauceDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Sauce.objects.all()
    serializer_class = SauceSerializer
    name = 'sauce-detail'
    filterset_fields = ['name', 'price']
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'price']


class Order_ClientView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Order_Client.objects.all()
    serializer_class = Order_ClientSerializer
    name = 'order_client-list'
    filterset_fields = ['pizza', 'sauce', 'client']
    ordering_fields = ['pizza', 'sauce', 'client']


class Order_ClientDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Order_Client.objects.all()
    serializer_class = Order_ClientSerializer
    name = 'order_client-detail'



class Order_RestaurantView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Order_Restaurant.objects.all()
    serializer_class = Order_RestaurantSerializer
    name = 'order_restaurant-list'
    filterset_fields = ['prize_order', 'date_realization']
    search_fields = ['prize_order', 'date_realization']
    ordering_fields = ['prize_order', 'date_realization']


class Order_RestaurantDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Order_Restaurant.objects.all()
    serializer_class = Order_RestaurantSerializer
    name = 'order_restaurant-detail'


class UserView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'Client': reverse(ClientView.name, request=request),
                         'Sauce': reverse(SauceView.name, request=request),
                         'Pizza': reverse(PizzaView.name, request=request),
                         'Driver': reverse(DriverView.name, request=request),
                         'Chef': reverse(ChefView.name, request=request),
                         'Order_Client': reverse(Order_ClientView.name, request=request),
                         'Order_Restaurant': reverse(Order_RestaurantView.name, request=request),
                         'Users': reverse(UserView.name, request=request)
                         })

from rest_framework import serializers
from .models import Pizza, Sauce, Chef, Driver, Client, Order_Restaurant, Order_Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'phone', 'address']


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['name', 'description', 'price']


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ['name', 'surname']


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['name', 'surname', 'phone']


class SauceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sauce
        fields = ['name', 'price']

class Order_ClientSerializer(serializers.ModelSerializer):
    pizza = serializers.SlugRelatedField(queryset=Pizza.objects.all(), slug_field='name')
    sauce = serializers.SlugRelatedField(queryset=Sauce.objects.all(), slug_field='name')
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='name')
    class Meta:
        model = Order_Client
        fields = ['pizza', 'sauce', 'client']

class Order_RestaurantSerializer(serializers.ModelSerializer):
    chef = serializers.SlugRelatedField(queryset=Chef.objects.all(), slug_field='name')
    driver = serializers.SlugRelatedField(queryset=Driver.objects.all(), slug_field='name')
    class Meta:
        model = Order_Restaurant
        fields = ['order_client', 'driver', 'chef', 'prize_order', 'date_realization']

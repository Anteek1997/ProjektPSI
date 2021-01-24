from rest_framework import serializers
from .models import Pizza, Sauce, Chef, Driver, Client, Order_Restaurant, Order_Client
from datetime import date
from django.contrib.auth.models import User


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    def validate_phone(self, value):
        if len(str(value)) != 9:
            raise serializers.ValidationError('Telefon musi składać sie z 9 cyfr.')
        return value

    class Meta:
        model = Client
        fields = ['pk', 'url', 'name', 'surname', 'phone', 'address']


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Cena nie może być ujemna.")
        return value

    class Meta:
        model = Pizza
        fields = ['pk', 'url', 'name', 'description', 'price']


class ChefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chef
        fields = ['pk', 'url', 'name', 'surname']


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    def validate_phone(self, value):
        if len(str(value)) != 9:
            raise serializers.ValidationError('Telefon musi składać sie z 9 cyfr.')
        return value

    class Meta:
        model = Driver
        fields = ['pk', 'url', 'name', 'surname', 'phone']


class SauceSerializer(serializers.HyperlinkedModelSerializer):
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Cena nie może być ujemna.")
        return value

    class Meta:
        model = Sauce
        fields = ['pk', 'url', 'name', 'price']


class Order_ClientSerializer(serializers.HyperlinkedModelSerializer):
    pizza = serializers.SlugRelatedField(queryset=Pizza.objects.all(), slug_field='name')
    sauce = serializers.SlugRelatedField(queryset=Sauce.objects.all(), slug_field='name')
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field="address")

    class Meta:
        model = Order_Client
        fields = ['pk', 'url', 'pizza', 'sauce', 'client']


class Order_RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    def validate_date_realization(self, value):
        if value < date.today():
            raise serializers.ValidationError("Data nie może być wcześniejsza od dzisiejszej.")
        return value

    chef = serializers.HyperlinkedRelatedField(queryset=Chef.objects.all(), view_name='chef-detail')
    driver = serializers.HyperlinkedRelatedField(queryset=Driver.objects.all(), view_name='driver-detail')

    class Meta:
        model = Order_Restaurant
        fields = ['pk', 'url', 'order_client', 'driver', 'chef', 'prize_order', 'date_realization']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'url', 'username', 'password', 'email']

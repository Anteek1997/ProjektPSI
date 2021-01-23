from rest_framework import serializers
from .models import Pizza, Sauce, Chef, Driver, Client, Order_Restaurant, Order_Client
from datetime import date


class ClientSerializer(serializers.ModelSerializer):
    def validate_phone(self, value):
        if len(str(value)) != 9:
            raise serializers.ValidationError('Telefon musi składać sie z 9 cyfr.')
        return value

    class Meta:
        model = Client
        fields = ['name', 'surname', 'phone', 'address']


class PizzaSerializer(serializers.ModelSerializer):
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Cena nie może być ujemna.")
        return value

    class Meta:
        model = Pizza
        fields = ['name', 'description', 'price']


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ['name', 'surname']


class DriverSerializer(serializers.ModelSerializer):
    def validate_phone(self, value):
        if len(str(value)) != 9:
            raise serializers.ValidationError('Telefon musi składać sie z 9 cyfr.')
        return value

    class Meta:
        model = Driver
        fields = ['name', 'surname', 'phone']


class SauceSerializer(serializers.ModelSerializer):
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Cena nie może być ujemna.")
        return value

    class Meta:
        model = Sauce
        fields = ['name', 'price']


class Order_ClientSerializer(serializers.ModelSerializer):
    pizza = serializers.SlugRelatedField(queryset=Pizza.objects.all(), slug_field='name')
    sauce = serializers.SlugRelatedField(queryset=Sauce.objects.all(), slug_field='name')
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field="address")

    class Meta:
        model = Order_Client
        fields = ['pizza', 'sauce', 'client']


class Order_RestaurantSerializer(serializers.ModelSerializer):
    def validate_date_realization(self, value):
        if value < date.today():
            raise serializers.ValidationError("Data nie może być wcześniejsza od dzisiejszej.")
        return value

    chef = serializers.SlugRelatedField(queryset=Chef.objects.all(), slug_field='name')
    driver = serializers.SlugRelatedField(queryset=Driver.objects.all(), slug_field='surname')


    class Meta:
        model = Order_Restaurant
        fields = ['order_client', 'driver', 'chef', 'prize_order', 'date_realization']

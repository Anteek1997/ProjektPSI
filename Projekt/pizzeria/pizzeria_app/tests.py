from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import Client, Pizza, Chef, Driver, Sauce
from rest_framework import status
from django.utils.http import urlencode
from django import urls


class ClientTests(APITestCase):
  def post_client(self, name, surname, phone, address):
    url = reverse(views.ClientView.name)
    data = {'name': name, 'surname': surname, 'phone': phone, 'address': address}
    response = self.client.post(url, data, format='json')
    return response

  def test_post_and_get_client(self):
    new_name = 'Adam'
    new_surname = "Sikorski"
    new_phone = 123123123
    new_address = "Ulica Sikorskiego 5/8 Olsztyn"
    response = self.post_client(new_name, new_surname, new_phone, new_address)

    assert response.status_code == status.HTTP_201_CREATED
    assert Client.objects.count() == 1
    assert Client.objects.get().name == new_name
    assert Client.objects.get().surname == new_surname
    assert Client.objects.get().phone == new_phone
    assert Client.objects.get().address == new_address

  def test_post_existing_client_name(self):
    new_name = 'Adam'
    new_surname = "Sikorski"
    new_phone = 123123123
    new_address = "Ulica Sikorskiego 5/8 Olsztyn"
    response_one = self.post_client(new_name, new_surname, new_phone, new_address)
    assert response_one.status_code == status.HTTP_201_CREATED
    response_two = self.post_client(new_name, new_surname, new_phone, new_address)
    assert response_two.status_code == status.HTTP_201_CREATED

  def test_filter_client_by_name(self):
    new_name = 'Adam'
    new_surname = "Sikorski"
    new_phone = 123123123
    new_address = "Ulica Sikorskiego 5/8 Olsztyn"

    new_name2 = 'Krzysztof'
    new_surname2 = "Rybka"
    new_phone2 = 823123123
    new_address2 = "Ulica Mickiewicza 3/1 Barczewo"

    self.post_client(new_name, new_surname, new_phone, new_address)
    self.post_client(new_name2, new_surname2, new_phone2, new_address2)
    filter_by_name = {'name': new_name, 'surname': new_surname}
    url = '{0}?{1}'.format(reverse(views.ClientView.name), urlencode(filter_by_name))
    response = self.client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
    assert response.data['results'][0]['name'] == new_name
    assert response.data['results'][0]['surname'] == new_surname
    assert response.data['results'][0]['phone'] == new_phone
    assert response.data['results'][0]['address'] == new_address


class PizzaTests(APITestCase):
  def post_pizza(self, name, description, price):
    url = reverse(views.PizzaView.name)
    data = {'name': name, 'description': description, 'price': price}
    response = self.client.post(url, data, format='json')
    return response

  def test_post_and_get_Pizza(self):
    new_name = 'Farmerska'
    new_description = 'Szynka'
    new_price = 35
    response = self.post_pizza(new_name, new_description, new_price)

    assert response.status_code == status.HTTP_201_CREATED
    assert Pizza.objects.count() == 1
    assert Pizza.objects.get().name == new_name
    assert Pizza.objects.get().description == new_description
    assert Pizza.objects.get().price == new_price

  def test_post_existing_pizza_name(self):
    new_name = 'Hawajska'
    new_description = 'Ananas'
    new_price = 25
    response_one = self.post_pizza(new_name, new_description, new_price)
    assert response_one.status_code == status.HTTP_201_CREATED
    response_two = self.post_pizza(new_name, new_description, new_price)
    assert response_two.status_code == status.HTTP_201_CREATED

  def test_filter_client_by_name(self):
    new_name = 'Hawajska'
    new_description = 'Ananas'
    new_price = 45

    new_name2 = 'Campione'
    new_description2 = 'Papryka'
    new_price2 = 35

    self.post_pizza(new_name, new_description, new_price)
    self.post_pizza(new_name2, new_description2, new_price2)
    filter_by_name = {'name': new_name}
    url = '{0}?{1}'.format(reverse(views.PizzaView.name), urlencode(filter_by_name))
    response = self.client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
    assert response.data['results'][0]['name'] == new_name

  def test_search_address(self):
    new_name = 'Farmerska'
    new_description = 'Szynka'
    new_price = 35
    self.post_pizza(new_name, new_description, new_price)
    search_pizza = {'name': new_name}
    url = '{0}?{1}'.format(reverse(views.PizzaView.name), urlencode(search_pizza))
    response = self.client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
    assert response.data['results'][0]['name'] == new_name


class ChefTests(APITestCase):
  def post_Chef(self, name, surname):
    url = reverse(views.ChefView.name)
    data = {'name': name, 'surname': surname}
    response = self.client.post(url, data, format='json')
    return response

  def test_post_and_get_Chef(self):
    new_name = 'Mateusz'
    new_surname = "Nowak"
    response = self.post_Chef(new_name, new_surname)

    assert response.status_code == status.HTTP_201_CREATED
    assert Chef.objects.count() == 1
    assert Chef.objects.get().name == new_name
    assert Chef.objects.get().surname == new_surname

  def test_post_existing_Chef_name(self):
    new_name = 'Mateusz'
    new_surname = "Nowak"
    response_one = self.post_Chef(new_name, new_surname)
    assert response_one.status_code == status.HTTP_201_CREATED
    response_two = self.post_Chef(new_name, new_surname)
    assert response_two.status_code == status.HTTP_201_CREATED

  def test_filter_Chef_by_name(self):
    new_name = 'Mateusz'
    new_surname = "Nowak"
    self.post_Chef(new_name, new_surname)
    filter_by_name = {'name': new_name}
    url = '{0}?{1}'.format(reverse(views.ChefView.name), urlencode(filter_by_name))
    response = self.client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
    assert response.data['results'][0]['name'] == new_name

  def test_search_Chef(self):
    new_name = 'Mateusz'
    new_surname = "Nowak"
    self.post_Chef(new_name, new_surname)
    search_Chef = {'name': new_name}
    url = '{0}?{1}'.format(reverse(views.ChefView.name), urlencode(search_Chef))
    response = self.client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
    assert response.data['results'][0]['name'] == new_name


class SauceTests(APITestCase):
  def post_Sauce(self, name, price):
    url = reverse(views.SauceView.name)
    data = {'name': name, 'price': price}
    response = self.client.post(url, data, format='json')
    return response

  def test_post_and_get_Sauce(self):
    new_name = 'Czosnkowy'
    new_price = 6

    response = self.post_Sauce(new_name, new_price)
    assert response.status_code == status.HTTP_201_CREATED
    assert Sauce.objects.count() == 1
    assert Sauce.objects.get().name == new_name
    assert Sauce.objects.get().price == new_price

  def test_post_existing_Sauce_name(self):
    new_name = 'Czosnkowy'
    new_price = 6
    response_one = self.post_Sauce(new_name, new_price)
    assert response_one.status_code == status.HTTP_201_CREATED
    response_two = self.post_Sauce(new_name, new_price)
    assert response_two.status_code == status.HTTP_201_CREATED

  def test_filter_Sauce_by_price(self):
    new_name = 'Czosnkowy'
    new_price = '6.00'
    self.post_Sauce(new_name, new_price)
    filter_by_price = {'price': new_price}
    url = '{0}?{1}'.format(reverse(views.SauceView.name), urlencode(filter_by_price))
    response = self.client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
    assert response.data['results'][0]['price'] == new_price

  def test_search_Sauce(self):
    new_name = 'Czosnkowy'
    new_price = '6.00'
    self.post_Sauce(new_name, new_price)
    search_Sauce = {'name': new_name}
    url = '{0}?{1}'.format(reverse(views.SauceView.name), urlencode(search_Sauce))
    response = self.client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
    assert response.data['results'][0]['name'] == new_name


class DriverTests(APITestCase):

  def post_Driver(self, name, surname, phone):
    url = reverse(views.DriverView.name)
    data = {'name': name, 'surname': surname, 'phone': phone}
    response = self.client.post(url, data, format='json')
    return response

  def test_post_and_get_Driver(self):
    new_name = 'Lukasz'
    new_surname = "Chomey"
    new_phone = 555555555
    response = self.post_Driver(new_name, new_surname, new_phone)
    assert response.status_code == status.HTTP_201_CREATED
    assert Driver.objects.count() == 1
    assert Driver.objects.get().name == new_name
    assert Driver.objects.get().phone == new_phone
    assert Driver.objects.get().surname == new_surname

  def test_search_surname_Driver(self):
    new_name = 'Lukasz'
    new_surname = "Chomey"
    new_phone = 555555555
    self.post_Driver(new_name, new_surname, new_phone)
    search_Driver = {'surname': new_surname}
    url = '{0}?{1}'.format(reverse(views.DriverView.name), urlencode(search_Driver))
    response = self.client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
    assert response.data['results'][0]['surname'] == new_surname



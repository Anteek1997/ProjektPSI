from django.db import models

class Pizza(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nazwa + ' ' + str(self.cena) + 'zl'


class Sos(models.Model):
    nazwa = models.CharField(max_length=50)
    cena = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.nazwa + ' ' + str(self.cena) + 'zl'

class Kucharz(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko

class Kierowca(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko

class Klient(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    telefon = models.IntegerField()
    adres = models.CharField(max_length=50)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko

class Zamowienie(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    kierowca = models.ForeignKey(Kierowca, on_delete=models.CASCADE)
    kucharz = models.ForeignKey(Kucharz, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    cena_zamowienia = models.DecimalField(max_digits=5,decimal_places=2)
    data_realizacji = models.DateField()
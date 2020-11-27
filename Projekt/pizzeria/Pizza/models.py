from django.db import models

class Pizza(models.Model):
    nazwa = models.CharField(max_length=50)
    opis =  models.TextField(blank=True)
    cena =  models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.nazwa + ' ' + str(self.cena) + 'zl'
from django.contrib import admin
from .models import Pizza, Sauce, Chef, Driver, Client, Order_Restaurant, Order_Client

admin.site.register(Pizza)
admin.site.register(Sauce)
admin.site.register(Chef)
admin.site.register(Driver)
admin.site.register(Client)
admin.site.register(Order_Client)
admin.site.register(Order_Restaurant)

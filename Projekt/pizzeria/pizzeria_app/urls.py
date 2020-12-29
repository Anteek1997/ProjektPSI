from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('widok/', views.index, name='index'),
    path('klient/', views.KlientView.as_view(), name=views.KlientView.name),
    path('klient/<int:pk>', views.KlientDetails.as_view()),
    path('pizza/', views.PizzaView.as_view(), name=views.PizzaView.name),
    path('pizza/<int:pk>', views.PizzaDetails.as_view()),
    path('kucharz/', views.KucharzView.as_view(), name=views.KucharzView.name),
    path('kucharz/<int:pk>', views.KucharzDetails.as_view()),
    path('kierowca/', views.KierowcaView.as_view(), name=views.KierowcaView.name),
    path('kierowca/<int:pk>', views.KierowcaDetails.as_view()),
    path('sos/', views.SosView.as_view(), name=views.SosView.name),
    path('sos/<int:pk>', views.SosDetails.as_view()),
    path('zamowienie/', views.ZamowienieView.as_view(), name=views.ZamowienieView.name),
    path('zamowienie/<int:pk>', views.ZamowienieDetails.as_view()),
]

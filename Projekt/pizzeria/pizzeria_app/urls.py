from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('klient/', views.KlientView.as_view()),
    path('klient/<int:pk>', views.KlientDetails.as_view()),
    path('pizza/', views.PizzaView.as_view()),
    path('pizza/<int:pk>', views.PizzaDetails.as_view()),
    path('kucharz/', views.KucharzView.as_view()),
    path('kucharz/<int:pk>', views.KucharzDetails.as_view()),
    path('kierowca/', views.KierowcaView.as_view()),
    path('kierowca/<int:pk>', views.KierowcaDetails.as_view()),
    path('sos/', views.SosView.as_view()),
    path('sos/<int:pk>', views.SosDetails.as_view()),
    path('zamowienie/', views.ZamowienieView.as_view()),
    path('zamowienie/<int:pk>', views.ZamowienieDetails.as_view()),
]
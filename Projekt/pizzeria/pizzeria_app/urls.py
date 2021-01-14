from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('view/', views.index, name='index'),
    path('client/', views.ClientView.as_view(), name=views.ClientView.name),
    path('client/<int:pk>', views.ClientDetails.as_view()),
    path('pizza/', views.PizzaView.as_view(), name=views.PizzaView.name),
    path('pizza/<int:pk>', views.PizzaDetails.as_view()),
    path('chef/', views.ChefView.as_view(), name=views.ChefView.name),
    path('chef/<int:pk>', views.ChefDetails.as_view()),
    path('driver/', views.DriverView.as_view(), name=views.DriverView.name),
    path('driver/<int:pk>', views.DriverDetails.as_view()),
    path('sauce/', views.SauceView.as_view(), name=views.SauceView.name),
    path('sauce/<int:pk>', views.SauceDetails.as_view()),
    path('order_client/', views.Order_ClientView.as_view(), name=views.Order_ClientView.name),
    path('order_client/<int:pk>', views.Order_ClientView.as_view()),
    path('order_restaurant/', views.Order_RestaurantView.as_view(), name=views.Order_RestaurantView.name),
    path('order_restaurant/<int:pk>', views.Order_RestaurantView.as_view()),
]

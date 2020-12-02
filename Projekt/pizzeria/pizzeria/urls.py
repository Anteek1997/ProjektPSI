from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizzeria_app/', include('pizzeria_app.urls')),
]

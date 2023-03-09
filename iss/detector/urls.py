from django.urls import path
from detector import views

urlpatterns = [
    path('', views.home),
]

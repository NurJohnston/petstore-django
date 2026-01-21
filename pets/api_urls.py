from django.urls import path
from .views import PetListCreateAPI, PetDetailAPI

urlpatterns = [
    path('pets/', PetListCreateAPI.as_view(), name='api_pets'),
    path('pets/<int:pk>/', PetDetailAPI.as_view(), name='api_pet_detail'),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('create/', views.pet_create, name='pet_create'),
    path('edit/<int:pk>/', views.pet_edit, name='pet_edit'),
    path('delete/<int:pk>/', views.pet_delete, name='pet_delete'),

    path('api/', include('pets.api_urls')),
]

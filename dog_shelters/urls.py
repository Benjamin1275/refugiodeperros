from django.urls import path
from . import views

urlpatterns = [
    path('shelters/', views.shelter_list, name='shelter_list'),
    path('shelters/<int:pk>/', views.shelter_detail, name='shelter_detail'),
    path('dogs/<int:pk>/', views.DogDetailView.as_view(), name='dog_detail'),
    path('dogs/new/', views.DogCreateView.as_view(), name='dog_new'),
]

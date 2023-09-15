from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('dna_sequence/', views.dna_sequence_list, name='dna_sequence_list'),
]
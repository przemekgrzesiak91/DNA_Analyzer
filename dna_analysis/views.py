from django.shortcuts import render
from .models import Project, DNASequence
# Create your views here.

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'dna_analysis/project_list.html', {'projects': projects})

def dna_sequence_list(request)
    #dodanie filtra zamiast czytanie wszytskich sekwencji (?)
    dna_sequences = DNASequence.objects.all()
    return render(request, 'dna_analysis/dna_sequence_list.html', {'dna_sequences' : dna_sequences})
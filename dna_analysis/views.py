from django.shortcuts import render
from .models import Project
# Create your views here.

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'dna_analysis/project_list.html', {'projects': projects})
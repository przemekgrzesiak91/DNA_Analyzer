from django.shortcuts import render

# Create your views here.

def project_list(request):
    return render(request, 'dna_analysis/project_list.html', {})
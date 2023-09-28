from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'dna_analysis/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'dna_analysis/project_detail.html', {'project': project})

def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'dna_analysis/project_edit.html', {'form': form})
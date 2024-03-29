from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import generic
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from .models import Project, DnaSequence
from .forms import ProjectForm, DnaSequenceForm


# Create your views here.
def project_list(request):
    projects = Project.objects.filter(author=request.user)
    paginator = Paginator(projects,5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dna_analysis/project_list.html', {'page_obj': page_obj})

def project_detail(request, pk):
    current_project = get_object_or_404(Project, pk=pk)
    dna_sequences = DnaSequence.objects.filter(project=current_project)

    return render(request, 'dna_analysis/project_detail.html', {'project': current_project, 'dna_sequences': dna_sequences})

def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'dna_analysis/project_edit.html', {'form': form})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'dna_analysis/project_edit.html', {'form': form})

@ensure_csrf_cookie
def project_delete(request, pk):
    project = get_object_or_404(Project,pk=pk)
    if request.user == project.author:
        try:
            project.delete()
            return redirect('project_list')
            #return JsonResponse({'status': 'success', 'message': 'Projekt został usunięty'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Wystąpił błąd podczas usuwania projektu.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Nie masz uprawnień do usunięcia tego projektu.'})

def dna_sequence_new(request, pk):
    if request.method == "POST":
        form = DnaSequenceForm(request.POST)
        if form.is_valid():
            sequence = form.save(commit=False)
            sequence.project = get_object_or_404(Project,pk=pk)
            sequence.save()

            return redirect('project_detail', pk=pk)
    else:
        form = DnaSequenceForm()
    return render(request, 'dna_analysis/dna_sequence_edit.html', {'form': form})

def dna_sequence_detail(request, pk):
    current_sequence = get_object_or_404(DnaSequence, pk=pk)

    return render(request, 'dna_analysis/dna_sequence_detail.html', {'sequence': current_sequence})

def dna_sequence_edit(request, pk):
    sequence = get_object_or_404(DnaSequence, pk=pk)
    if request.method == "POST":
        form = DnaSequenceForm(request.POST, instance=sequence)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('project_detail', pk=sequence.project.pk)
    else:
        form = DnaSequenceForm(instance=sequence)
    return render(request, 'dna_analysis/project_edit.html', {'form': form})

@ensure_csrf_cookie
def dna_sequence_delete(request, pk):
    pass
    sequence = get_object_or_404(DnaSequence,pk=pk)
    if request.user == sequence.project.author:
        try:
            sequence.delete()
            return redirect('project_detail', pk=sequence.project.pk)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Wystąpił błąd podczas usuwania projektu.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Nie masz uprawnień do usunięcia tego projektu.'})



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
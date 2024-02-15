from django import forms
from .models import Project, DnaSequence

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description')

# class DnaSequenceForm(forms.ModelForm):
#     class Meta:
#         model = DnaSequence
#         fields = ('project', 'description')
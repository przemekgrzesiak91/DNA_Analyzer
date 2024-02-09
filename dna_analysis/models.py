from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class DnaSequence(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    sequence = models.TextField()
    length = models.PositiveIntegerField()

    # stosunek G/C
    # typ sekwencji?
    # w zasadzie czytanie jej czyli wklej sekwencej (FASTa/ itp) i rozloz ja na czesci i uzupełni pola.)?


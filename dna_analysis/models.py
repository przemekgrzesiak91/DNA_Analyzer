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

    name = models.CharField(max_length=100)
    sequence = models.TextField()
    length = models.PositiveIntegerField(blank=True, null=True)

    def seq_length (self, *args, **kwargs):
        self.length = len(self.sequence)
        super().seq_length(*args, **kwargs)

    def __str__(self):
        return self.name

    # stosunek G/C
    # typ sekwencji?
    # w zasadzie czytanie jej czyli wklej sekwencej (FASTa/ itp) i rozloz ja na czesci i uzupełni pola.)?




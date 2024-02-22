# Generated by Django 4.2.6 on 2024-02-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dna_analysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dnasequence',
            name='description',
        ),
        migrations.AddField(
            model_name='dnasequence',
            name='name',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
    ]

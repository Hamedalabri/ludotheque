# Generated by Django 5.0.6 on 2024-05-26 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_jeu_auteur_alter_jeu_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='type_personne',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
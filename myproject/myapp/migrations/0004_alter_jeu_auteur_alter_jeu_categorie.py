# Generated by Django 5.0.6 on 2024-05-26 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_jeu_annee_sortie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jeu',
            name='auteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.auteur'),
        ),
        migrations.AlterField(
            model_name='jeu',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.categorie'),
        ),
    ]

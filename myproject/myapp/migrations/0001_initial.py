# Generated by Django 5.0.6 on 2024-05-26 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('photos', models.ImageField(blank=True, null=True, upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('descriptif', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Joueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=254)),
                ('mot_de_passe', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jeu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('annee_sortie', models.IntegerField()),
                ('photo_boite', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('editeur', models.CharField(max_length=200)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.auteur')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField()),
                ('commentaire', models.TextField()),
                ('jeu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.jeu')),
                ('joueur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.joueur')),
            ],
        ),
    ]

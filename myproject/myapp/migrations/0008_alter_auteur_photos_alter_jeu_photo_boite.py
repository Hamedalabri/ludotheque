# Generated by Django 5.0.6 on 2024-05-26 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_commentaire_type_personne'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auteur',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='jeu',
            name='photo_boite',
            field=models.ImageField(blank=True, null=True, upload_to='photo_boite'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-27 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_commentaire_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='note',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)]),
        ),
    ]
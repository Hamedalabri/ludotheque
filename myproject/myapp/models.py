from datetime import datetime
from statistics import mode
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    descriptif = models.TextField()

    def __str__(self):
        return self.nom

class Auteur(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    age = models.IntegerField()
    photos = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.nom

class Jeu(models.Model):
    titre = models.CharField(max_length=200)
    annee_sortie = models.IntegerField(default=2000)
    photo_boite = models.ImageField(upload_to='photo_boite', blank=True, null=True)
    editeur = models.CharField(max_length=200)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titre

class Joueur(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    mail = models.EmailField()
    mot_de_passe = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=[('professionnel', 'Professionnel'), ('particulier', 'Particulier')])

    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    jeu = models.ForeignKey(Jeu, on_delete=models.CASCADE)
    joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    note = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default=0)
    commentaire = models.TextField()
    #type_personne = models.CharField(max_length=100, default='unknown')


    def __str__(self):
        return f"{self.joueur} - {self.date}"
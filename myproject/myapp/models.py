from django.db import models

# Create your models here.

from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    descriptif = models.TextField()

class Auteur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    age = models.IntegerField()
    photos = models.ImageField()

class Jeu(models.Model):
    titre = models.CharField(max_length=255)
    annee_sortie = models.IntegerField()
    photo_boite = models.ImageField()
    editeur = models.CharField(max_length=255)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

class Joueur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    mail = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=[('professionnel', 'Professionnel'), ('particulier', 'Particulier')])

class Commentaire(models.Model):
    jeu = models.ForeignKey(Jeu, on_delete=models.CASCADE)
    joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class ListeJeux(models.Model):
    joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE)
    jeu = models.ForeignKey(Jeu, on_delete=models.CASCADE)

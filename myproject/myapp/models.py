from statistics import mode
from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    descriptif = models.TextField()

    def __str__(self):
        return self.nom

class Auteur(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    age = models.IntegerField()
    photos = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.nom

class Jeu(models.Model):
    titre = models.CharField(max_length=200)
    annee_sortie = models.IntegerField()
    photo_boite = models.ImageField(upload_to='photos/', blank=True, null=True)
    editeur = models.CharField(max_length=200)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

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
    note = models.IntegerField()
    commentaire = models.TextField()


    #def __str__(self):
      #  return f"{self.} - {self.}"

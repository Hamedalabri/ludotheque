from django import forms
from .models import Categorie, Auteur, Jeu, Joueur, Commentaire

class CategorieForm(forms.ModelForm):
    class Meta:
         model = Categorie
         fields = {'nom','descriptif'}
         labels = {
            'nom': ('le nom de la catégorie de jeux'),
            'descriptif': ('le descriptif de la catégorie')
        }

class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = {'nom','prenom','age','photos'}
        labels = {
            'nom': ("nom de l'auteur"),
            'prenom': ("prenom de l'auteur"),
            'age': ("age de l'auteur"),
            'photos': ("photo de l'auteur")
        }

class JeuForm(forms.ModelForm):
    class Meta:
        model = Jeu
        fields = ['titre', 'annee_sortie', 'photo_boite', 'editeur', 'auteur', 'categorie']
        labels = {
            'titre': ('Titre du jeu'),
            'annee_sortie':("L'année de sortie du jeu"),
            'photo_boite':("Une photo de la boite"),
            'editeur':("l'éditeur du jeu"),
            'auteur': ("l'auteur du jeu"),
            'categorie': ("La catégorie du jeu"),
        }

class JoueurForm(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = ['nom', 'prenom', 'mail', 'mot_de_passe', 'type']
        widgets = {
            'mot_de_passe': forms.PasswordInput(),
        }
        

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['jeu', 'joueur', 'note', 'commentaire', ]
        labels = {
            'note': ('Note sur /20'),
        }

class UploadFileForm(forms.Form):
    file = forms.FileField()
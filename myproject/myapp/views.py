from django.shortcuts import render, get_object_or_404, redirect
from .models import Categorie, Auteur, Jeu, Joueur, Commentaire
from .forms import CategorieForm, AuteurForm, JeuForm, JoueurForm, CommentaireForm , UploadFileForm
from django.db.models import Avg
import csv



def home(request):
    return render(request, 'home.html')

# les catégories
def display_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, pk=categorie_id)
    return render(request, 'categorie/display_categorie.html', {'categorie': categorie})

def categorieList(request):
    categories = Categorie.objects.all()
    return render(request,'categorie/categorie_liste.html',{'categories': categories})

def categorie_create(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorie-liste')
    else:
        form = CategorieForm()
    return render(request, 'categorie/categorie_create.html', {'form': form})

def categorie_update(request, id):
    categorie = get_object_or_404(Categorie, pk=id)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('categorie-liste')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'categorie/categorie_update.html', {'form': form})

def categorie_delete(request, id):
    categorie = get_object_or_404(Categorie, pk=id)
    categorie.delete()
    return redirect('categorie-liste')

def jeux_liste_par_categorie(request, categorie_nom):
    categorie = Categorie.objects.get(nom=categorie_nom)
    jeux = Jeu.objects.filter(categorie=categorie)
    return render(request, 'jeu/jeux_liste.html', {'jeux': jeux, 'categorie': categorie})

# les auteurs
def display_auteur(request, auteur_id):
    auteur = get_object_or_404(Auteur, pk=auteur_id)
    return render(request, 'auteur/display_auteur.html', {'auteur': auteur})

def auteurList(request):
    auteurs = Auteur.objects.all()
    return render(request,'auteur/auteur_liste.html',{'auteurs': auteurs})

def auteur_create(request):
    if request.method == 'POST':
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auteur-liste')
    else:
        form = AuteurForm()
    return render(request, 'auteur/auteur_create.html', {'form': form})

def auteur_update(request, id):
    auteur = get_object_or_404(Auteur, pk=id)
    if request.method == 'POST':
        form = AuteurForm(request.POST, instance=auteur)
        if form.is_valid():
            form.save()
            return redirect('auteur-liste')
    else:
        form = AuteurForm(instance=auteur)
    return render(request, 'auteur/auteur_update.html', {'form': form})

def auteur_delete(request, id):
    auteur = get_object_or_404(Auteur, pk=id)
    auteur.delete()
    return redirect('auteur-liste')

# les jeux
def display_jeu(request, jeu_id):
    jeu = get_object_or_404(Jeu, pk=jeu_id)
    commentaires = Commentaire.objects.filter(jeu=jeu)

    moyenne_notes = commentaires.aggregate(moyenne=Avg('note'))['moyenne']
    commentaire_max = commentaires.order_by('-note').first()
    commentaire_min = commentaires.order_by('note').first()

    context = {
        'jeu': jeu,
        'commentaires': commentaires,
        'moyenne_notes': moyenne_notes,
        'commentaire_max': commentaire_max,
        'commentaire_min': commentaire_min,
    }
    return render(request, 'jeu/display_jeu.html', context)

    #return render(request, 'jeu/display_jeu.html', {'jeu': jeu})

def jeuList(request):
    jeux = Jeu.objects.all()
    return render(request,'jeu/jeux_liste.html',{'jeux': jeux})

def jeu_create(request):
    if request.method == 'POST':
        form = JeuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jeu-liste')
    else:
        form = JeuForm()
    return render(request, 'jeu/jeu_create.html', {'form': form})

def jeu_update(request, id):
    jeu = get_object_or_404(Jeu, pk=id)
    if request.method == 'POST':
        form = JeuForm(request.POST, instance=jeu)
        if form.is_valid():
            form.save()
            return redirect('jeu-liste')
    else:
        form = JeuForm(instance=jeu)
    return render(request, 'jeu/jeu_update.html', {'form': form})

def jeu_delete(request, id):
    jeu = get_object_or_404(Jeu, pk=id)
    jeu.delete()
    return redirect('jeu-liste')

# les joueurs
def display_joueur(request, joueur_id):
    joueur = get_object_or_404(Joueur, pk=joueur_id)
    commentaires = Commentaire.objects.filter(joueur=joueur)
    jeux_commented = Jeu.objects.filter(commentaire__in=commentaires).distinct()

    context = {
        'joueur': joueur,
        'jeux_commented': jeux_commented,
        'commentaires': commentaires,
    }
    return render(request, 'joueur/display_joueur.html', context)
    #return render(request, 'joueur/display_joueur.html', {'joueur': joueur})

def joueurList(request):
    joueurs = Joueur.objects.all()
    return render(request,'joueur/joueur_liste.html',{'joueurs': joueurs})

def joueur_create(request):
    if request.method == 'POST':
        form = JoueurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('joueur-liste')
    else:
        form = JoueurForm()
    return render(request, 'joueur/joueur_create.html', {'form': form})

def joueur_update(request, id):
    joueur = get_object_or_404(Joueur, pk=id)
    if request.method == 'POST':
        form = JoueurForm(request.POST, instance=joueur)
        if form.is_valid():
            form.save()
            return redirect('joueur-liste')
    else:
        form = JoueurForm(instance=joueur)
    return render(request, 'joueur/joueur_update.html', {'form': form})

def joueur_delete(request, id):
    joueur = get_object_or_404(Joueur, pk=id)
    joueur.delete()
    return redirect('joueur-liste')

# les commentaires
def display_commentaire(request, commentaire_id):
    commentaire = get_object_or_404(Commentaire, pk=commentaire_id)
    return render(request, 'commentaire/display_commentaire.html', {'joueur': commentaire})

def commentaireList(request):
    commentaires = Commentaire.objects.all()
    return render(request,'commentaire/commentaire_liste.html',{'commentaires': commentaires})

def commentaire_create(request):
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commentaire-liste')
    else:
        form = CommentaireForm()
    return render(request, 'commentaire/commentaire_create.html', {'form': form})

def commentaire_update(request, id):
    commentaire = get_object_or_404(Commentaire, pk=id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            return redirect('commentaire-liste')
    else:
        form = CommentaireForm(instance=commentaire)
    return render(request, 'commentaire/commentaire_update.html', {'form': form})

def commentaire_delete(request, id):
    commentaire = get_object_or_404(Commentaire, pk=id)
    commentaire.delete()
    return redirect('commentaire-liste')



# Uploads

def handle_uploaded_file(f):
    reader = csv.reader(f)
    for row in reader:
        titre, annee_sortie, photo_boite, editeur, auteur_nom, auteur_prenom, categorie_id = row
        auteur, created = Auteur.objects.get_or_create(nom=auteur_nom, prenom=auteur_prenom)
        categorie = get_object_or_404(Categorie, id=categorie_id)
        Jeu.objects.create(titre=titre, annee_sortie=annee_sortie, photo_boite=photo_boite, editeur=editeur, auteur=auteur, categorie=categorie)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('jeu-liste')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
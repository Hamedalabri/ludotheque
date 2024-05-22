from django.shortcuts import render, get_object_or_404, redirect
from .models import Categorie, Auteur, Jeu, Joueur, Commentaire
from .forms import CategorieForm, AuteurForm, JeuForm, JoueurForm, CommentaireForm

# les catégories


def categorieList(request):
    categories = Categorie.objects.all()
    return render(request,'categorie_liste.html',{'categories': categories})


def categorie_create(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorie-liste')
    else:
        form = CategorieForm()
    return render(request, 'categorie_create.html', {'form': form})

def categorie_update(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('categorie-liste')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'categorie_create.html', {'form': form})

def categorie_delete(request, id):
    categorie = get_object_or_404(Categorie, pk=id)
    categorie.delete()
    return render('categorie-liste')








# les auteurs

def aueturList(request):
    auteurs = Auteur.objects.all()
    return render(request,'auteur_liste.html',{'auteurs': auteurs})

def auteur_create(request):
    if request.method == 'POST':
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auteur-liste')
    else:
        form = AuteurForm()
    return render(request, 'auteur_create.html', {'form': form})

def auteur_update(request, id):
    auteur = get_object_or_404(Auteur, id=id)
    if request.method == 'POST':
        form = AuteurForm(request.POST, instance=auteur)
        if form.is_valid():
            form.save()
            return redirect('auteur-liste')
    else:
        form = AuteurForm(instance=auteur)
    return render(request, 'auteur_update.html', {'form': form})

def auteur_delete(request, id):
    auteur = get_object_or_404(Auteur, pk=id)
    auteur.delete()
    return render('auteur-liste')





# les jeux

def jeuList(request):
    jeux = Jeu.objects.all()
    return render(request,'jeux_liste.html',{'jeux': jeux})

def jeu_create(request):
    if request.method == 'POST':
        form = JeuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jeux-liste')
    else:
        form = JeuForm()
    return render(request, 'jeu_create.html', {'form': form})

def jeu_update(request, id):
    jeu = get_object_or_404(Jeu, id=id)
    if request.method == 'POST':
        form = JeuForm(request.POST, instance=jeu)
        if form.is_valid():
            form.save()
            return redirect('jeux-liste')
    else:
        form = JeuForm(instance=jeu)
    return render(request, 'jeu_update.html', {'form': form})

def jeu_delete(request, id):
    jeu = get_object_or_404(Jeu, pk=id)
    jeu.delete()
    return render('Jeux-liste')



#les joueurs

def joueurList(request):
    joueurs = Joueur.objects.all()
    return render(request,'joueur_liste.html',{'joueurs': joueurs})

def joueur_create(request):
    if request.method == 'POST':
        form = JoueurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('joueur-liste')
    else:
        form = JoueurForm()
    return render(request, 'joueur_create.html', {'form': form})

def joueur_update(request, id):
    joueur = get_object_or_404(Joueur, id=id)
    if request.method == 'POST':
        form = JoueurForm(request.POST, instance=joueur)
        if form.is_valid():
            form.save()
            return redirect('joueur-liste')
    else:
        form = JoueurForm(instance=joueur)
    return render(request, 'joueur_update.html', {'form': form})

def joueur_delete(request, id):
    joueur = get_object_or_404(Joueur, id=id)
    joueur.delete()
    return render('joueur-liste')





# les commentaires

def commentaireList(request):
    commentaires = Commentaire.objects.all()
    return render(request,'commentaire_liste.html',{'commentaires': commentaires})

def commentaire_create(request):
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commentaire-liste')
    else:
        form = CommentaireForm()
    return render(request, 'commentaire_create.html', {'form': form})

def commentaire_update(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            return redirect('commentaire-liste')
    else:
        form = CommentaireForm(instance=commentaire)
    return render(request, 'commentaire_update.html', {'form': form})

def commentaire_delete(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)
    commentaire.delete()
    return render('commentaire-liste')

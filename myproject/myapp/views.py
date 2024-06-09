from django.shortcuts import render, get_object_or_404, redirect
from .models import Categorie, Auteur, Jeu, Joueur, Commentaire
from .forms import CategorieForm, AuteurForm, JeuForm, JoueurForm, CommentaireForm , UploadFileForm
from django.db.models import Avg
import csv
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet , ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.units import inch


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
        form = AuteurForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('auteur-liste')
    else:
        form = AuteurForm()
    return render(request, 'auteur/auteur_create.html', {'form': form})

def auteur_update(request, id):
    auteur = get_object_or_404(Auteur, pk=id)
    if request.method == 'POST':
        form = AuteurForm(request.POST, request.FILES, instance=auteur)
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
        form = JeuForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jeu-liste')
    else:
        form = JeuForm()
    return render(request, 'jeu/jeu_create.html', {'form': form})

def jeu_update(request, id):
    jeu = get_object_or_404(Jeu, pk=id)
    if request.method == 'POST':
        form = JeuForm(request.POST, request.FILES ,instance=jeu)
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

def joueur_pdf_view(request, pk):
    joueur = Joueur.objects.get(pk=pk)
    commentaires = Commentaire.objects.filter(joueur=joueur)
    jeux_commented = {commentaire.jeu for commentaire in commentaires}

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="joueur_{joueur.nom}.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Set default font and size
    font_size = 12
    p.setFont("Helvetica", font_size)

    # Draw things on the PDF. Here's where the PDF generation happens.
    p.drawString(100, height - 50, f"Nom: {joueur.nom}")
    p.drawString(100, height - 70, f"Prenom: {joueur.prenom}")
    p.drawString(100, height - 90, f"Mail: {joueur.mail}")
    p.drawString(100, height - 110, f"Type: {joueur.type}")

    p.drawString(100, height - 130, "Jeux commentés:")
    y = height - 150
    for jeu in jeux_commented:
        p.drawString(120, y, f"- {jeu.titre}")
        y -= 20

    p.drawString(100, y - 20, "Commentaires:")
    y -= 40

    styles = getSampleStyleSheet()
    comment_style = ParagraphStyle(
        'Comment',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=font_size,
        leading=font_size + 2,
        spaceAfter=10,
    )

    for commentaire in commentaires:
        p.drawString(120, y, f"{commentaire.jeu.titre}: {commentaire.note}/20")
        y -= 20

        text = commentaire.commentaire
        paragraph = Paragraph(text, comment_style)
        text_width, text_height = paragraph.wrap(width - 140, y)
        if y - text_height < 0:
            p.showPage()
            p.setFont("Helvetica", font_size)
            y = height - 50
            p.drawString(100, y, "Commentaires (suite):")
            y -= 20

        paragraph.drawOn(p, 120, y - text_height)
        y -= text_height + 20

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    return response

# les commentaires
def display_commentaire(request, commentaire_id):
    commentaire = get_object_or_404(Commentaire, pk=commentaire_id)
    return render(request, 'commentaire/display_commentaire.html', {'commentaire': commentaire})

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
def handle_uploaded_file(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        auteur, created = Auteur.objects.get_or_create(
            nom=row['auteur_nom'],
            prenom=row['auteur_prenom'],
            defaults={'age': row.get('auteur_age', None)}
        )
        if not created and row.get('auteur_age'):
            auteur.age = row['auteur_age']
            auteur.save()
        
        try:
            categorie = Categorie.objects.get(id=row['categorie_id'])
        except Categorie.DoesNotExist:
            print(f"Skipping row due to missing category: {row}")
            continue
        
        Jeu.objects.create(
            titre=row['titre'],
            annee_sortie=row['annee_sortie'],
            photo_boite=row['photo_boite'],
            editeur=row['editeur'],
            auteur=auteur,
            categorie=categorie
        )

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('jeu-liste')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def home(request):
    jeu = Jeu.objects.first()  
    return render(request, 'home.html', {'jeu': jeu})
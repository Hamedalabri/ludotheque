from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    # categories
    path('categories/', views.categorieList, name='categorie-liste'),
    path('categories/create/', views.categorie_create, name='create_categorie'),
    path('categories/update/<int:id>/', views.categorie_update, name='update_categorie'),
    path('categories/delete/<int:id>/', views.categorie_delete, name='delete_categorie'),
    path('categories/<int:categorie_id>/', views.display_categorie, name='display_categorie'),

    # auteurs
    path('auteurs/', views.auteurList, name='auteur-liste'),
    path('auteurs/create/', views.auteur_create, name='create_auteur'),
    path('auteurs/update/<int:id>/', views.auteur_update, name='update_auteur'),
    path('auteurs/delete/<int:id>/', views.auteur_delete, name='delete_auteur'),
    path('auteurs/<int:auteur_id>/', views.display_auteur, name='display_auteur'),

    # jeux
    path('jeux/', views.jeuList, name='jeu-liste'),
    path('jeux/create/', views.jeu_create, name='create_jeu'),
    path('jeux/update/<int:id>/', views.jeu_update, name='update_jeu'),
    path('jeux/delete/<int:id>/', views.jeu_delete, name='delete_jeu'),
    path('jeux/<int:jeu_id>/', views.display_jeu, name='display_jeu'),
    path('jeu-list/categorie/<str:categorie_nom>/', views.jeux_liste_par_categorie, name='jeux-liste-par-categorie'),

    # joueurs
    path('joueurs/', views.joueurList, name='joueur-liste'),
    path('joueurs/create/', views.joueur_create, name='create_joueur'),
    path('joueurs/update/<int:id>/', views.joueur_update, name='update_joueur'),
    path('joueurs/delete/<int:id>/', views.joueur_delete, name='delete_joueur'),
    path('joueurs/<int:joueur_id>/', views.display_joueur, name='display_joueur'),

    # commentaires
    path('commentaires/', views.commentaireList, name='commentaire-liste'),
    path('commentaires/create/', views.commentaire_create, name='create_commentaire'),
    path('commentaires/update/<int:id>/', views.commentaire_update, name='update_commentaire'),
    path('commentaires/delete/<int:id>/', views.commentaire_delete, name='delete_commentaire'),
    path('commentaires/<int:commentaire_id>/', views.display_commentaire, name='display_commentaire'),

    # upload
    path('jeux/upload/', views.upload_file, name='upload_file'),
]

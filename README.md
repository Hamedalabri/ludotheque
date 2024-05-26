sujet 3 : ludothèque
Conditions d’achèvement
ce sujet va vous permettre de fournir une interface de gestion d'une ludothèque. Les usagers pourront commenter les jeux et les ajouter dans leur liste personnelle. Le schéma de données est le suivant

des catégories de jeux (id, nom, descriptif)
des jeux (id, titre, année de sortie, photo boite, éditeur, auteur,  catégorie)
des auteurs (id, nom, prénom, âge, photos)
des joueurs (id, nom prénom, mail, mot de passe, type => professionnel ou particulier)
des commentaires sur les jeux (Jeux, Joueurs, note,  commentaire, date)
une liste de jeux pour les usagers
Vous devez implémenter un CRUD pour chacun de ces types de données. vous préparerez la base en avance et la remplirez avec des catégories, des jeux et des auteurs.

Votre site web devra permettre la saisie de nouveaux usagers et des commentaires qu'ils font sur les jeux. vous calculerez pour chaque jeu la moyenne des notes pour chaque type de personnes commentant. vous devrez aussi mettre en avant les commentaires avec le plus haute note et avec la plus basse note sur la page de chaque jeux.

 Vous devrez aussi pouvoir insérer de nouveau jeux à l'aide d'un fichier. Si l'auteur n'existe pas, il sera crée avec le nom et le prénom La structure du fichier attendu devra bien sur être décrite soit dans une aide, soit en préambule de la page de chargement.

Vous devrez être à même de pouvoir générer une fiche pour un joueur, avec sa liste de jeux et les commentaires qu'il a pu faire sur chaque jeux ainsi que la note moyenne du jeu



Veuilez utiliser la commnade :"cd myproject", avant démarrer le serveur.
Pour accéder à la page film-list.html, veuillez utiliser le lien suivant :http://127.0.0.1:8000/
projet de Hamed AL-ABRI

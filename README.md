# Astral Shooter – Jeu de tir gravitationnel (Pygame)

Ce projet est un jeu de tir en Pygame où le joueur contrôle un canon pour détruire des météorites à l’aide de tirs à trajectoire parabolique.  
L'angle est contrôlé avec la souris, la puissance dépend de la durée d’appui sur le clic.  
Trois niveaux sont proposés, chacun avec une gravité différente (Terre, Lune, Jupiter).

Le but est de survivre le plus longtemps possible sans que le personnage ne perde toutes ses vies.

## Fonctionnalités
- 3 niveaux avec gravité variable
- Mode facile : plus de vies et trajectoire prévisualisée
- Contrôle de l’angle avec la souris
- Contrôle de la puissance avec la durée du clic
- Sauvegarde automatique du meilleur score (facile & normal)
- Menu principal, mise en pause du jeu, affichage des règles du jeu

## Fichiers
- `main.pyw` : fichier principal du jeu
- `constantes.py` : toutes les constantes du jeu
- `fonctions_calcul.py` : fonctions liées à la trajectoire et la physique
- `images/` : tous les sprites, décors et éléments visuels
- `meilleur_score_facile.txt` / `meilleur_score_normal.txt` : meilleurs scores par mode

## Lancer le jeu

Assurez-vous d’avoir Python 3 et Pygame installés.

```bash
python main.pyw
```

---

*Projet réalisé en mai 2024, mis en ligne ici en juin 2025.*

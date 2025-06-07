"""
"Astral Shooter"

Ce fichier contient l'ensemble des constantes définies pour le jeu, que ce soit les images chargées à l'écran, la position de chaque éléments placés ou même la vitesse de tir du canon par exemple.
"""

import sys
from pathlib import Path

# Obtient le chemin du répertoire de main.pyw
CHEMIN_MAIN = Path(__file__).resolve().parent
sys.path.append(str(CHEMIN_MAIN))


import pygame

pygame.init()


LARGEUR_FENETRE, HAUTEUR_FENETRE = 1280, 500


# Import de toutes les images ##############################

ICONE_JEU = pygame.image.load(f"{CHEMIN_MAIN}/images/icone_jeu.png")


IMAGE_DECOR_ACCUEIL = pygame.image.load(f"{CHEMIN_MAIN}/images/decors/fond_accueil.png")

IMAGE_DECOR_PREMIER_NIVEAU = pygame.image.load(f"{CHEMIN_MAIN}/images/decors/fond_premier_niveau.png")
IMAGE_DECOR_DEUXIEME_NIVEAU = pygame.image.load(f"{CHEMIN_MAIN}/images/decors/fond_deuxieme_niveau.png")
IMAGE_DECOR_TROISIEME_NIVEAU = pygame.image.load(f"{CHEMIN_MAIN}/images/decors/fond_troisieme_niveau.png")

LISTE_DECORS_NIVEAU = [IMAGE_DECOR_PREMIER_NIVEAU, IMAGE_DECOR_DEUXIEME_NIVEAU, IMAGE_DECOR_TROISIEME_NIVEAU]

IMAGE_FOND_MENUS = pygame.image.load(f"{CHEMIN_MAIN}/images/decors/fond_menus.png")


IMAGE_TEXTE_MODE_ON = pygame.image.load(f"{CHEMIN_MAIN}/images/textes/texte_mode_facile_on.png")
IMAGE_TEXTE_MODE_OFF = pygame.image.load(f"{CHEMIN_MAIN}/images/textes/texte_mode_facile_off.png")
IMAGE_TEXTE_NOM_JEU = pygame.image.load(f"{CHEMIN_MAIN}/images/textes/texte_nom_jeu.png")
IMAGE_TEXTE_CLIQUEZ = pygame.image.load(f"{CHEMIN_MAIN}/images/textes/texte_cliquez.png")

IMAGE_TEXTE_NIVEAU_SUIVANT = pygame.image.load(f"{CHEMIN_MAIN}/images/textes/texte_niveau_suivant.png")
IMAGE_TEXTE_REESSAYER = pygame.image.load(f"{CHEMIN_MAIN}/images/textes/texte_reessayer.png")
IMAGE_TEXTE_ECHOUAGE = pygame.image.load(f"{CHEMIN_MAIN}/images/textes/texte_echouage.png")


IMAGE_CANON_SANS_ROUE = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_jeu/canon_sans_roue.png")
IMAGE_ROUE_CANON = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_jeu/roue_canon.png")
IMAGE_BOULET_CANON = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_jeu/boulet_canon.png")
IMAGE_JAUGE_TIR = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_jeu/jauge.png")
IMAGE_FLECHE_JAUGE = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_jeu/fleche_jauge.png")
IMAGE_EXPLOSION = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_jeu/explosion.png")
IMAGE_COEUR_ROUGE = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_jeu/coeur_rouge.png")
IMAGE_COEUR_NOIR = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_jeu/coeur_noir.png")
IMAGE_PERSONNAGE = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_jeu/personnage.png")
IMAGE_METEORITE = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_jeu/meteorite.png")
IMAGE_BLESSURE = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_jeu/blessure.png")


IMAGE_FOND_PAUSE = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/menu_pause.png")

IMAGE_BOUTON_JOUER = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/bouton_jouer.png")
IMAGE_EFFET_BOUTON = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/effet_bouton.png")
IMAGE_CASE_ENCOCHE = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/case_encoche.png")
IMAGE_CASE_ENCOCHE_EFFET = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/case_encoche_effet.png")
IMAGE_ENCOCHE_VERTE = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/encoche_verte.png")
IMAGE_REGLES = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/regles.png")
IMAGE_REGLES_EFFET = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/regles_effet.png")
IMAGE_CROIX = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/croix_rouge.png")
IMAGE_CROIX_EFFET = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/croix_rouge_effet.png")

IMAGE_BOUTON_RETOUR_ACC_EFFET = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/bouton_retour_acc_effet.png")
IMAGE_BOUTON_RETOUR_ACC = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/bouton_retour_acc.png")
IMAGE_BOUTON_REESSAYER_EFFET = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/bouton_reessayer_effet.png")
IMAGE_BOUTON_REESSAYER = pygame.image.load(f"{CHEMIN_MAIN}/images/elements_menus/bouton_reessayer.png")


# Valeurs constantes

# Principales

# Définition de la police de caractères utilisée dans le jeu
POLICE_JEU = "Century Gothic"

# Nombre d'images par seconde pour l'affichage
IMAGES_PAR_SECONDE = 60

# Rectangle pour l'affichage du nom du jeu
TEXTE_NOM_JEU_RECT = IMAGE_TEXTE_NOM_JEU.get_rect()
TEXTE_NOM_JEU_RECT.center = LARGEUR_FENETRE // 2, 110

# Dimensions du bouton "Jouer"
DIMENSION_IMAGE_BOUTON = 150

# Décalage pour l'affichage du bouton "Jouer" et du texte "Cliquez pour jouer"
DECALAGE_BOUTON_HAUT = HAUTEUR_FENETRE // 2 + 65

# Rectangle pour l'affichage du texte "Cliquez pour jouer"
TEXTE_CLIQUEZ_RECT = IMAGE_TEXTE_CLIQUEZ.get_rect()
TEXTE_CLIQUEZ_RECT.center = LARGEUR_FENETRE // 2, DECALAGE_BOUTON_HAUT + DIMENSION_IMAGE_BOUTON // 2 + 50

# Rectangle pour le bouton "Jouer"
BOUTON_JOUER_RECT = IMAGE_BOUTON_JOUER.get_rect()
BOUTON_JOUER_RECT.center = LARGEUR_FENETRE // 2, DECALAGE_BOUTON_HAUT

# Rectangle pour l'effet de survol du bouton "Jouer"
EFFET_BOUTON_RECT = IMAGE_EFFET_BOUTON.get_rect()
EFFET_BOUTON_RECT.center = BOUTON_JOUER_RECT.center

# Dimensions de l'encoche pour le mode de jeu
LARGEUR_ENCOCHE, HAUTEUR_ENCOCHE = 40, 34

# Largeur du texte pour le mode facile
LARGEUR_TEXTE_MODE_FACILE = 217

# Rectangle pour l'affichage de l'encoche
ENCOCHE_RECT = IMAGE_CASE_ENCOCHE.get_rect()
ENCOCHE_RECT.x, ENCOCHE_RECT.y = 20, HAUTEUR_FENETRE - (HAUTEUR_ENCOCHE + 10)

# Rectangle pour l'effet de survol de l'encoche
ENCOCHE_EFFET_RECT = IMAGE_CASE_ENCOCHE_EFFET.get_rect()
ENCOCHE_EFFET_RECT.center = ENCOCHE_RECT.center

# Rectangle pour l'affichage du texte du mode facile
TEXTE_MODE_FACILE_RECT = IMAGE_TEXTE_MODE_ON.get_rect()
TEXTE_MODE_FACILE_RECT.center = LARGEUR_TEXTE_MODE_FACILE // 2 + LARGEUR_ENCOCHE + 6, ENCOCHE_RECT.center[1] - 1

# Dimension de l'image des règles
DIMENSION_IMAGE_REGLES = 115

# Rectangle pour l'affichage de l'image des règles
REGLES_RECT = IMAGE_REGLES.get_rect()
REGLES_RECT.bottomright = LARGEUR_FENETRE - 2, HAUTEUR_FENETRE

# Rectangle pour l'affichage du cadre des règles
SURFACE_REGLES_RECT = pygame.Rect(40, 30, LARGEUR_FENETRE - 80, HAUTEUR_FENETRE - 60)

# Dimension de l'image de la croix rouge
DIMENSION_CROIX_ROUGE = 40

# Rectangle pour l'affichage de la croix rouge
CROIX_RECT = IMAGE_CROIX.get_rect()
CROIX_RECT.center = SURFACE_REGLES_RECT.topright[0] - 30, SURFACE_REGLES_RECT.topright[1] + 30

# Rectangle pour l'effet de survol de la croix rouge
CROIX_EFFET_RECT = IMAGE_CROIX_EFFET.get_rect()
CROIX_EFFET_RECT.center = CROIX_RECT.center

# Coordonnées du texte des règles
COORDONNEES_TEXTE_REGLES = SURFACE_REGLES_RECT.topleft[0] + 20, SURFACE_REGLES_RECT.topleft[1] + 10

# Hauteur du texte des règles
HAUTEUR_TEXTE_REGLES = 20

# Police de caractères pour le texte des règles
POLICE_TEXTE_REGLES = pygame.font.SysFont(POLICE_JEU, HAUTEUR_TEXTE_REGLES)

# Liste du texte des règles
TEXTE_REGLES = ["- Le jeu s'intitule \"Astral Shooter\" et tourne autour des planètes.",
                "- Le joueur contrôle l'angle de tir d'un canon avec le déplacement de la souris, et la puissance de"
                "tir",
                "   avec la durée d'enfoncement du clic (relâcher pour tirer), et doit détruire les météorites pour "
                "protéger l'individu.",
                "   Lorsque l'individu reçoit un boulet de canon ou une météorite, il perd une vie; il ne faut surtout "
                "pas toutes les perdres !",
                "- Le menu principal permet d'activer le mode facile qui augmente le nombre de vie et qui affiche",
                "   une pré-visualisation de la trajectoire de tir.",
                "- Le joueur peut, à tout moment, mettre le jeu en pause en appuyant sur la touche Entrée,",
                "   et revenir en jeu en ré-appuyant sur cette touche (ou la touche Échap pour quitter)",
                "- Un score (correspondant aux millisecondes durant lesquelles le joueur a survécu) augmente",
                "   et indique l'avancée du joueur; essayez d'atteindre la plus haute valeur possible !",
                "- Pour que le meilleur score soit sauvegardé,",
                "   assurez-vous d'être retourné au menu principal (ou d'avoir perdu) avant de quitter le jeu.",
                "- Le jeu se décompose en 3 parties :",
                "    > La première planète sur lequel le joueur apparaît a une gravité semblable à celle sur Terre",
                "    > La deuxième planète a une gravité semblable à celle sur Lune",
                "    > La troisième planète a une gravité semblable à celle de Jupiter; il faut survivre le plus "
                "longtemps possible !"
                ]

# Décalage pour l'affichage des boutons en cas de défaite
DECALAGE_POS_X_BOUTONS_PERDU = 230
DECALAGE_POS_Y_BOUTONS_PERDU = 125

# Rectangle pour l'affichage du bouton "Rejouer"
BOUTON_REESSAYER_RECT = IMAGE_BOUTON_REESSAYER.get_rect()
BOUTON_REESSAYER_RECT.center = LARGEUR_FENETRE // 2 + DECALAGE_POS_X_BOUTONS_PERDU, \
    HAUTEUR_FENETRE // 2 + DECALAGE_POS_Y_BOUTONS_PERDU

# Rectangle pour l'affichage du bouton "Retour à l'accueil" en cas de défaite
BOUTON_RETOUR_ACC_PERDU_RECT = IMAGE_BOUTON_RETOUR_ACC.get_rect()
BOUTON_RETOUR_ACC_PERDU_RECT.center = LARGEUR_FENETRE // 2 - DECALAGE_POS_X_BOUTONS_PERDU, \
    HAUTEUR_FENETRE // 2 + DECALAGE_POS_Y_BOUTONS_PERDU

# Dimensions des boutons de menu
LARGEUR_BOUTON_MENU = 420
HAUTEUR_BOUTON_MENU = 150

# Décalage pour l'affichage du texte en cas d'échec
DECALAGE_TEXTE_ECHOUAGE = 90

# Rectangle pour l'affichage du texte en cas d'échec
TEXTE_ECHOUAGE_RECT = IMAGE_TEXTE_ECHOUAGE.get_rect()
TEXTE_ECHOUAGE_RECT.center = LARGEUR_FENETRE // 2, DECALAGE_TEXTE_ECHOUAGE

# Décalage pour l'affichage du texte de "Rejouer"
DECALAGE_TEXTE_REESSAYER = 200

# Rectangle pour l'affichage du texte de "Rejouer"
TEXTE_RESSAYER_RECT = IMAGE_TEXTE_REESSAYER.get_rect()
TEXTE_RESSAYER_RECT.center = LARGEUR_FENETRE // 2, DECALAGE_TEXTE_REESSAYER


# En jeu

# Intensité de la pesanteur pour chaque niveau
INTENSITE_PESANTEUR_NIVEAU = [9.81, 1.62, 20]

# Décalage en x du canon par rapport au bord de la fenêtre
DECALAGE_X_CANON = 25

# Dimensions de l'image du canon et position initiale en x et y
LARGEUR_IMAGE_CANON = 175
POS_X_CANON = DECALAGE_X_CANON - LARGEUR_IMAGE_CANON // 4 - 10
POS_Y_CANON = HAUTEUR_FENETRE - LARGEUR_IMAGE_CANON + 25

# Rectangle du canon sans roue et position du centre
CANON_SANS_ROUE_RECT = IMAGE_CANON_SANS_ROUE.get_rect()
CANON_SANS_ROUE_RECT.x, CANON_SANS_ROUE_RECT.y = POS_X_CANON, POS_Y_CANON
POSTION_CENTRE_CANON_SANS_ROUE = CANON_SANS_ROUE_RECT.center

# Vitesse minimale et maximale du boulet, ainsi que l'incrément de vitesse et le multiplicateur de vitesse
VITESSE_BOULET_MIN = 60
VITESSE_BOULET_MAX = 140
INCREMENTATION_VITESSE = 0.83
MULTIPLICATEUR_VITESSE = 1.2

# Diviseur de vitesse pour le tir du boulet
DIVISEUR_VITESSE = 5

# Décalage du boulet par rapport au canon
DECALAGE_BOULET = 10

# Position en x et y de la roue du canon
POS_X_ROUE_CANON = DECALAGE_X_CANON + 30
POS_Y_ROUE_CANON = HAUTEUR_FENETRE - 80

# Angle minimal et maximal de tir, ainsi que le rayon du canon pour le tir
ANGLE_TIR_MINIMAL = 0.2
ANGLE_TIR_MAXIMAL = 1.1
RAYON_CANON_TIR = LARGEUR_IMAGE_CANON // 2 - 13

# Décalage de la jauge et position du centre de la flèche de la jauge
DECALAGE_JAUGE = 20
ANGLE_LIMITE_DIMINUTION = -5
ANGLE_ROTATION_INITAL = 1
ANGLE_ROTATION_MAXIMAL = 177

DIMENSION_JAUGE = 100

# Rectangle de la flèche de la jauge et position du centre
FLECHE_JAUGE_RECT = IMAGE_FLECHE_JAUGE.get_rect()
FLECHE_JAUGE_RECT.x, FLECHE_JAUGE_RECT.y = DECALAGE_JAUGE, DECALAGE_JAUGE
POSITION_CENTRE_FLECHE_JAUGE = FLECHE_JAUGE_RECT.center

# Valeur de diminution de la flèche de la jauge
DIMINUTION_FLECHE_JAUGE = 10

# Épaisseur des zones de collision (sol, mur, plafond)
EPAISSEUR_COLLISION = 300
HAUTEUR_SOL_COLLISION = HAUTEUR_FENETRE - 50
SOL_RECT = pygame.Rect(0, HAUTEUR_SOL_COLLISION, LARGEUR_FENETRE,
                       HAUTEUR_FENETRE + EPAISSEUR_COLLISION - HAUTEUR_SOL_COLLISION)

LARGEUR_MUR_COLLISION = LARGEUR_FENETRE + EPAISSEUR_COLLISION
MUR_RECT = pygame.Rect(LARGEUR_FENETRE, 0, LARGEUR_MUR_COLLISION, HAUTEUR_FENETRE)

HAUTEUR_PLAFOND_COLLISION = -100
PLAFOND_RECT = pygame.Rect(0, HAUTEUR_PLAFOND_COLLISION, LARGEUR_FENETRE + EPAISSEUR_COLLISION,
                           HAUTEUR_PLAFOND_COLLISION - EPAISSEUR_COLLISION)

# Durée de l'explosion
DUREE_EXPLOSION = 200

# Nombre de vies initial pour chaque mode de jeu
NOMBRE_VIES_INITIAL_MODE_NORMAL = 5
NOMBRE_VIES_INITIAL_MODE_FACILE = 7

# Dimensions et position des cœurs représentant les vies du joueur
LARGEUR_COEUR = 30
POS_X_DERNIER_COEUR = LARGEUR_FENETRE - LARGEUR_COEUR - 25
POS_Y_COEUR = 20
DECALAGE_COEUR = LARGEUR_COEUR + 10

# Dimensions du personnage et position initiale en x et y
LARGEUR_PERSONNAGE = 29
HAUTEUR_PERSONNAGE = 140
PERSONNAGE_RECT = IMAGE_PERSONNAGE.get_rect()
PERSONNAGE_RECT.x, PERSONNAGE_RECT.y = LARGEUR_FENETRE - 45 - LARGEUR_PERSONNAGE, \
    HAUTEUR_FENETRE + HAUTEUR_SOL_COLLISION - HAUTEUR_FENETRE - HAUTEUR_PERSONNAGE

# Dimension des météorites et intervalle de positionnement en x
DIMENSION_METEORITE = 28
INTERVALLE_POS_X_METEORITES = [100, 800]
POS_Y_METEORITES = 0

# Vitesse des météorites
VITESSE_METEORITE = 3

# Nombre de météorites pour chaque niveau
NOMBRE_METEORITES_NIVEAU = [10, 15]

DELAI_APPARITION_METEORITE = 1

# Largeur du marqueur de trajectoire et positions début et fin
LARGEUR_MARQUEUR_TRAJECTOIRE = 5
POS_DEBUT_MARQUEUR_TRAJ = 10
AJOUT_POS_MARQUEUR_TRAJ = 30
POS_FIN_MARQUEUR_TRAJ = 350

# Recul en cas de blessure du personnage
RECUL_BLESSURE = 25

# Coordonnées du texte de pause et hauteur du texte
COORDONNEES_TEXTE_PAUSE = 415, 395
HAUTEUR_TEXTE_MENU_PAUSE = 18

# Délai avant l'affichage de l'écran du niveau suivant
DELAI_NIVEAU_SUIVANT = 2000

# Rectangle pour l'affichage du texte de niveau suivant
TEXTE_NIVEAU_SUIVANT_RECT = IMAGE_TEXTE_NIVEAU_SUIVANT.get_rect()
TEXTE_NIVEAU_SUIVANT_RECT.center = LARGEUR_FENETRE // 2, HAUTEUR_FENETRE // 2

# Police utilisée pour le texte du menu pause
POLICE_TEXTE_MENU_PAUSE = pygame.font.SysFont(POLICE_JEU, HAUTEUR_TEXTE_MENU_PAUSE)

# Texte affiché dans le menu pause
TEXTE_MENU_PAUSE = ["Le jeu est en pause.",
                    "- Appuyez sur Entrée pour relancer le jeu",
                    "- Appuyez sur Echap pour quitter le jeu",
                    ]

NOM_FICHIER_MEILLEUR_SCORE_NORMAL = f"{CHEMIN_MAIN}/meilleur_score_normal.txt"
NOM_FICHIER_MEILLEUR_SCORE_FACILE = f"{CHEMIN_MAIN}/meilleur_score_facile.txt"

HAUTEUR_TEXTE_SCORE = 16

POLICE_TEXTE_SCORES = pygame.font.SysFont(POLICE_JEU, HAUTEUR_TEXTE_SCORE)

TEXTE_SCORE_ACTUEL_POS_Y = DIMENSION_JAUGE
TEXTE_MEILLEUR_SCORE_POS_Y = TEXTE_SCORE_ACTUEL_POS_Y + 25

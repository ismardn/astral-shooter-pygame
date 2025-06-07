"""
"Astral Shooter"

Ce fichier contient toutes les fonctions de "calcul", notamment la trajectoire de tir et celle des météorites, ou même l'actualisation de la postion d'une météorite, par exemple.
"""


from constantes import *
import math
import random
import pygame


def fonction_trajectoire_boulet(x, alpha, v0, g):
    """
    Calcule la trajectoire d'un projectile en fonction de plusieurs paramètres.

    :param x: La distance horizontale parcourue par le projectile.
    :param alpha: L'angle de tir en radians.
    :param v0: La vitesse initiale du projectile.
    :param g: L'accélération gravitationnelle.
    :return: La hauteur atteinte par le projectile à une distance donnée.
    """
    # Calcul de la hauteur de la trajectoire en fonction de la distance horizontale x
    hauteur = (-1 / 2) * g * (x / (v0 * math.cos(alpha))) ** 2 + x * math.tan(alpha)

    return hauteur


def fonction_trajectoire_meteorite(x, composants_meteorite):
    """
    Calcule la hauteur à laquelle se trouve une météorite à une position x donnée sur l'écran.

    :param x: Position horizontale sur l'écran où la hauteur de la météorite est calculée (float).
    :param composants_meteorite: Dictionnaire contenant les composants de la météorite,
    notamment ses coordonnées initiales (dict).

    :return: Hauteur de la météorite à la position x spécifiée (float).
    """
    # Récupération de la position initiale en x de la météorite depuis le dictionnaire de composants
    position_x_initiale_meteorite = composants_meteorite["coordonnees_initiales"][0]

    # Calcul du coefficient directeur de la trajectoire, basé sur la position initiale de la météorite et du personnage
    coefficient_directeur_traj = (PERSONNAGE_RECT.center[1] - POS_Y_METEORITES) / \
                                 (PERSONNAGE_RECT.center[0] - position_x_initiale_meteorite)

    # Calcul de la hauteur à laquelle la météorite se trouve à une position donnée 'x' sur l'écran
    hauteur = coefficient_directeur_traj * x + POS_Y_METEORITES -\
        coefficient_directeur_traj * position_x_initiale_meteorite

    return hauteur


def creer_meteorite(liste_meteorites):
    """
    Crée une nouvelle météorite et l'ajoute à la liste des météorites existantes.

    :param liste_meteorites: Liste des météorites existantes (list).
    :return: Liste mise à jour des météorites, avec la nouvelle météorite ajoutée (list).
    """
    # Obtention des positions initiales en x de toutes les météorites existantes
    positions_x_initiales = []
    for composants_meteorite in liste_meteorites:
        positions_x_initiales.append(composants_meteorite["coordonnees_initiales"][0])

    # Choix d'une position initiale x pour la nouvelle météorite, en évitant les positions déjà occupées
    position_x_meteorite = random.choice([
        position_x
        for position_x in range(INTERVALLE_POS_X_METEORITES[0], INTERVALLE_POS_X_METEORITES[1],
                                DIMENSION_METEORITE)
        if position_x not in positions_x_initiales
    ])

    # Création du rectangle pour la nouvelle météorite
    meteorite_rect = IMAGE_METEORITE.get_rect()
    meteorite_rect.x, meteorite_rect.y = (position_x_meteorite, POS_Y_METEORITES)

    # Création du rectangle de collision pour la nouvelle météorite
    collision_meteorite_rect = pygame.Rect(0, 0, DIMENSION_METEORITE, DIMENSION_METEORITE)
    collision_meteorite_rect.center = meteorite_rect.center

    # Ajout des informations de la nouvelle météorite à la liste des météorites
    liste_meteorites.append({
        "coordonnees_initiales": (position_x_meteorite, POS_Y_METEORITES),
        "rect_meteorite": meteorite_rect,
        "rect_zone_collision": collision_meteorite_rect,
        "coordonnees_actuelles": [position_x_meteorite, POS_Y_METEORITES],
    })

    return liste_meteorites


def actualiser_pos_meteorite(composants_meteorite):
    """
    Actualise la position de la météorite en fonction de sa trajectoire.

    :param composants_meteorite: Dictionnaire contenant les composants de la météorite à actualiser (dict).
    :return: Dictionnaire des composants de la météorite avec les positions actualisées (dict).
    """
    # Calcul des nouvelles positions x et y en fonction de la vitesse de déplacement de la météorite
    nouvelle_pos_x = composants_meteorite["coordonnees_actuelles"][0] + VITESSE_METEORITE
    nouvelle_pos_y = int(fonction_trajectoire_meteorite(nouvelle_pos_x, composants_meteorite))

    # Mise à jour des coordonnées actuelles de la météorite
    composants_meteorite["coordonnees_actuelles"] = [nouvelle_pos_x, nouvelle_pos_y]

    # Mise à jour du rectangle de la météorite avec les nouvelles positions
    meteorite_rect = composants_meteorite["rect_meteorite"]
    meteorite_rect.x, meteorite_rect.y = nouvelle_pos_x, nouvelle_pos_y
    composants_meteorite["rect_meteorite"] = meteorite_rect

    # Mise à jour du rectangle de collision de la météorite avec les nouvelles positions
    zone_collision_rect = composants_meteorite["rect_zone_collision"]
    zone_collision_rect.center = meteorite_rect.center
    composants_meteorite["rect_zone_collision"] = zone_collision_rect

    return composants_meteorite


def angle_tir_canon(position_x, position_y):
    """
    Calcule l'angle de tir du canon en fonction de la position du joueur.

    :param position_x: La coordonnée x de la position du joueur.
    :param position_y: La coordonnée y de la position du joueur.
    :return: L'angle de tir du canon.
    """
    # Calcul des longueurs des côtés du triangle formé par le joueur et le centre du canon
    longueur_adjacent = position_x - POSTION_CENTRE_CANON_SANS_ROUE[0]
    longueur_oppose = POSTION_CENTRE_CANON_SANS_ROUE[1] - position_y

    # Calcul de la longueur de l'hypoténuse du triangle
    longueur_hypotenuse = math.sqrt(longueur_adjacent ** 2 + longueur_oppose ** 2)

    # Calcul de l'angle de tir en radians
    angle_tir = math.acos(longueur_adjacent / longueur_hypotenuse)

    # Limite l'angle de tir entre les valeurs minimales et maximales spécifiées
    if angle_tir < ANGLE_TIR_MINIMAL:
        angle_tir = ANGLE_TIR_MINIMAL
    elif angle_tir > ANGLE_TIR_MAXIMAL:
        angle_tir = ANGLE_TIR_MAXIMAL

    return angle_tir


def calculer_score(nombre_millisecondes):
    """
    Calcule le score à partir du nombre de millisecondes écoulées, arrondi à la demi-seconde la plus proche.

    :param nombre_millisecondes: Le nombre de millisecondes écoulées.
    :return: Le score calculé arrondi à la demi-seconde la plus proche.
    """
    # Arrondir le nombre de millisecondes à la seconde inférieure la plus proche
    nombre_millisecondes_arrondi = (nombre_millisecondes // 1000) * 1000

    # Si les millisecondes restantes après la division par 1000 sont inférieures à 500,
    # le score est simplement l'arrondi précédent.
    if nombre_millisecondes % 1000 < 500:
        return nombre_millisecondes_arrondi
    # Sinon, le score est l'arrondi précédent plus 500.
    else:
        return nombre_millisecondes_arrondi + 500


def lecture_fichier_score(fichier_score):
    """
    Lit le fichier contenant le meilleur score du jeu.

    Si le fichier n'existe pas, il est créé avec un score initial de 0.
    Si le fichier existe déjà, son contenu est lu et renvoyé.

    :param fichier_score: Nom du fichier contenant le score du joueur.
    :return: Le meilleur score lu à partir du fichier.
    """
    try:
        # Tentative d'ouverture du fichier en mode "x+" (lecture/écriture, création s'il n'existe pas)
        with open(fichier_score, "x+") as fichier:
            # Si le fichier est créé, écrire un score initial de 0
            fichier.write("0")
            return 0
    except FileExistsError:
        # Si le fichier existe déjà

        with open(fichier_score, "r") as fichier:
            contenu_fichier = fichier.read()

        with open(fichier_score, "w") as fichier:
            try:
                score = int(contenu_fichier)
                fichier.write(contenu_fichier)
                return score
            except ValueError:
                # En cas d'erreur de conversion, écrire un score initial de 0 et le renvoyer
                fichier.write("0")
                return 0


def comparer_score(score_actuel, meilleur_score, fichier_score):
    """
    Compare le score actuel avec le meilleur score enregistré. Si le score actuel est inférieur ou égal au meilleur
    score, retourne simplement le meilleur score. Sinon, met à jour le fichier de score avec le nouveau score actuel
    et retourne ce dernier.

    :param score_actuel: Le score actuel du joueur.
    :param meilleur_score: Le meilleur score enregistré précédemment.
    :param fichier_score: Le nom du fichier où enregistrer le score.
    :return: Le meilleur score après comparaison.
    """
    if score_actuel <= meilleur_score:
        return meilleur_score  # Retourne le meilleur score si le score actuel est inférieur ou égal
    else:
        with open(fichier_score, "w") as fichier:
            fichier.write(str(score_actuel))  # Met à jour le fichier de score avec le nouveau score actuel
        return score_actuel  # Retourne le nouveau score actuel après mise à jour

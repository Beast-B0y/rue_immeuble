"""
Projet Rue d'Immeubles - Version 2
Nom : Evan Hanquez
Classe : Première NSI
Fichier : evan_hanquez_v2.py
"""

from turtle import *
import random
import time

# ==============================================================================
# CONFIGURATION INITIALE
# ==============================================================================
setup(0.9, 0.9)
title("Projet Rue d'Immeubles - Version 2")
hideturtle()
tracer(5, 1)

temps_pause = 3  # Temps de pause en secondes entre chaque dessin


# ==============================================================================
# FONCTIONS DE TRACÉ
# ==============================================================================

def tracer_fond():
    """Rempli le fond de l'écran avec la couleur du ciel."""
    bgcolor("skyblue")


def tracer_cadre(marge_cadre, largeur_ecran, hauteur_ecran):
    """
    Trace le cadre du dessin.
    - marge_cadre = 'a'
    - largeur_ecran = 'l' (1920)
    - hauteur_ecran = 'h' (1080)
    """
    x_min = -largeur_ecran / 2 + marge_cadre  # -l/2 + a
    y_min = -hauteur_ecran / 2 + marge_cadre  # -h/2 + a
    largeur_cadre = largeur_ecran - 2 * marge_cadre  # l - 2*a
    hauteur_cadre = hauteur_ecran - 2 * marge_cadre  # h - 2*a

    penup()
    goto(x_min, y_min)
    setheading(0)
    color("black")
    pensize(3)
    pendown()

    for _ in range(2):
        forward(largeur_cadre)
        left(90)
        forward(hauteur_cadre)
        left(90)

    penup()


def rue_evan(x_depart, y_depart, marge_cadre, hauteur_rue, largeur_ecran, nombre_immeubles):
    """
    Dessine la rue en bas du dessin.
    - x_depart, y_depart : Coordonnées du coin inférieur gauche de la rue
    - marge_cadre = 'a'
    - hauteur_rue = 'b'
    - largeur_ecran = 'l'
    - nombre_immeubles = 'Nb_im'
    """
    largeur_rue = largeur_ecran - 2 * marge_cadre  # l_rue = l - 2*a
    epaisseur_trait = 11 - nombre_immeubles  # Épaisseur du trait selon le nombre d'immeubles

    # 1. Tracé du bitume
    penup()
    goto(x_depart, y_depart)
    setheading(0)
    color("black", "grey")
    pensize(epaisseur_trait)
    pendown()
    begin_fill()
    for _ in range(2):
        forward(largeur_rue)
        left(90)
        forward(hauteur_rue)
        left(90)
    end_fill()

    # 2. Pointillés au milieu de la rue
    penup()
    goto(x_depart, y_depart + hauteur_rue / 2)
    color("yellow")
    pensize(max(1, epaisseur_trait // 2))

    pos_x = x_depart
    while pos_x < (x_depart + largeur_rue):
        pendown()
        forward(15)
        penup()
        forward(10)
        pos_x += 25

    penup()


def tracer_contour_rectangle(x, y, largeur, hauteur, couleur_fond="white"):
    """Trace un rectangle représentant le contour d'un niveau (RDC ou étage)."""
    penup()
    goto(x, y)
    setheading(0)
    color("black", couleur_fond)
    pensize(2)
    pendown()
    begin_fill()
    for _ in range(2):
        forward(largeur)
        left(90)
        forward(hauteur)
        left(90)
    end_fill()
    penup()


def tracer_immeubles(x_rue, y_rue, marge_cadre, hauteur_rue, largeur_ecran, hauteur_ecran, nombre_immeubles):
    """
    Trace les contours de tous les immeubles (RDC + étages).
    - marge_extremite_rue = 'c'
    - espace_entre_immeubles = 'd'
    - largeur_immeuble = 'e' (e = (l_rue - 2*c - (Nb_im - 1)*d) / Nb_im)
    - hauteur_etage = 'h_f' (h_f = e / 2)
    - nombre_immeubles = 'Nb_im'
    """
    largeur_rue = largeur_ecran - 2 * marge_cadre  # l_rue = l - 2*a
    marge_extremite_rue = 20  # 'c'
    espace_entre_immeubles = 20  # 'd'

    # Largeur d'un immeuble 'e'
    largeur_immeuble = (largeur_rue - 2 * marge_extremite_rue - (nombre_immeubles - 1) * espace_entre_immeubles) / nombre_immeubles

    # Hauteur d'un étage 'h_f = e / 2' ajustée pour ne pas dépasser du cadre
    hauteur_disponible = (hauteur_ecran / 2 - marge_cadre) - (y_rue + hauteur_rue)
    hauteur_etage = min(largeur_immeuble / 2, (hauteur_disponible - 40) / nombre_immeubles)

    x_immeuble = x_rue + marge_extremite_rue  # Position X de départ du 1er immeuble
    y_immeuble = y_rue + hauteur_rue  # Position Y posée sur le haut de la rue

    for _ in range(nombre_immeubles):
        # Le nombre de niveaux (RDC inclus) est entre 1 et nombre_immeubles (Nb_im)
        nombre_niveaux = random.randint(1, nombre_immeubles)

        for niveau in range(nombre_niveaux):
            y_niveau = y_immeuble + (niveau * hauteur_etage)
            tracer_contour_rectangle(x_immeuble, y_niveau, largeur_immeuble, hauteur_etage, "white")

        # Avancer X pour placer l'immeuble suivant : e + d
        x_immeuble += largeur_immeuble + espace_entre_immeubles


# ==============================================================================
# BOUCLE PRINCIPALE (Dessiner -> Attendre -> Effacer -> Recommencer)
# ==============================================================================

marge_cadre = 30  # 'a'
hauteur_rue = 60  # 'b'

while True:
    largeur_ecran = window_width()  # 'l'
    hauteur_ecran = window_height()  # 'h'

    x_depart = -largeur_ecran / 2 + marge_cadre  # -l/2 + a
    y_depart = -hauteur_ecran / 2 + marge_cadre  # -h/2 + a

    # Nombre d'immeubles aléatoire entre 3 et 10 ('Nb_im')
    nombre_immeubles = random.randint(3, 10)

    # 1. Dessiner
    tracer_fond()
    tracer_cadre(marge_cadre, largeur_ecran, hauteur_ecran)
    rue_evan(x_depart, y_depart, marge_cadre, hauteur_rue, largeur_ecran, nombre_immeubles)
    tracer_immeubles(x_depart, y_depart, marge_cadre, hauteur_rue, largeur_ecran, hauteur_ecran, nombre_immeubles)
    update()

    # 2. Attendre
    time.sleep(temps_pause)

    # 3. Effacer
    clear()
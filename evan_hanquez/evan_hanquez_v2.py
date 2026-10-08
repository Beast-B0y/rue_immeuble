"""
Projet Rue d'Immeubles - Version 1
Nom : Evan Hanquez
Classe : Terminale  NSI
Fichier : evan_hanquez_v2.py
"""

from turtle import *
from random import * 
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

# ==============================================================================
# BOUCLE PRINCIPALE (Dessiner -> Attendre -> Effacer -> Recommencer)
# ==============================================================================

marge_cadre = 30  # 'a'
hauteur_rue = 60  # 'b'

while True:
    nombre_immeubles = randint(3,10)
    largeur_ecran = window_width()  # 'l'
    hauteur_ecran = window_height()  # 'h'
    x_depart = -largeur_ecran / 2 + marge_cadre  # -l/2 + a
    y_depart = -hauteur_ecran / 2 + marge_cadre  # -h/2 + a
    # 1. Dessiner
    tracer_fond()
    tracer_cadre(marge_cadre, largeur_ecran, hauteur_ecran)
    rue_evan(x_depart, y_depart, marge_cadre, hauteur_rue, largeur_ecran, nombre_immeubles)
    update()
    # 2. Attendre
    time.sleep(temps_pause)
    # 3. Effacer
    clear()
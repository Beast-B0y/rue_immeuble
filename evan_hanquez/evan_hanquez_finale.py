import random
import time
from turtle import *

setup(0.9, 0.9)
title("Projet Rue d'Immeubles - Evan")
hideturtle()

tracer(5, 1)
speed(6)

colormode(255)  # Mode RVB de 0 a 255

temps_pause = 3


# ==============================================================================
# MODULE EVAN
# ==============================================================================


def fenetre_evan(x, y, taille, nombre_immeubles):
    penup()
    goto(x, y)
    setheading(0)
    color("black", "lightblue")
    pensize(max(1, int(11 - nombre_immeubles)))
    pendown()
    begin_fill()
    for _ in range(4):
        forward(taille)
        left(90)
    end_fill()
    penup()

    goto(x + taille / 2, y)
    color("brown")
    pensize(max(1, int(0.75 * (11 - nombre_immeubles))))
    setheading(90)
    pendown()
    forward(taille)
    penup()

    goto(x, y + taille / 2)
    setheading(0)
    pendown()
    forward(taille)
    penup()


def porte_evan(x, y, taille, nombre_immeubles):
    penup()
    goto(x, y)
    setheading(0)
    color("black", "grey")
    pensize(max(1, int(11 - nombre_immeubles)))
    pendown()
    begin_fill()
    for _ in range(2):
        forward(taille)
        left(90)
        forward(taille * 2)
        left(90)
    end_fill()
    penup()

    goto(x + taille * 0.1, y + taille * 0.9)
    color("black", "lightblue")
    pensize(max(1, int(0.5 * (11 - nombre_immeubles))))
    setheading(0)
    pendown()
    begin_fill()
    for _ in range(2):
        forward(taille * 0.8)
        left(90)
        forward(taille * 0.9)
        left(90)
    end_fill()
    penup()

    goto(x + taille * 0.1, y + taille * 0.6)
    color("black")
    pensize(max(1, int(0.5 * (11 - nombre_immeubles))))
    setheading(0)
    pendown()
    forward(taille * 0.2)
    penup()


# ==============================================================================
# MODULE LORIS
# ==============================================================================


def fenetre_loris(x, y, taille, nombre_immeubles):
    penup()
    goto(x, y)
    setheading(0)
    color("black", "lightgreen")
    pensize(2)
    pendown()
    begin_fill()
    for _ in range(4):
        forward(taille)
        left(90)
    end_fill()
    penup()


def porte_loris(x, y, taille, nombre_immeubles):
    penup()
    goto(x, y)
    setheading(0)
    color("black", "pink")
    pensize(2)
    pendown()
    begin_fill()
    for _ in range(2):
        forward(taille)
        left(90)
        forward(taille * 2)
        left(90)
    end_fill()
    penup()


# ==============================================================================
# MODULE REMY
# ==============================================================================


def fenetre_remy(x, y, taille, nombre_immeubles):
    penup()
    goto(x, y)
    setheading(0)
    color("black", "deepskyblue")
    pensize(2)
    pendown()
    begin_fill()
    for _ in range(4):
        forward(taille)
        left(90)
    end_fill()
    penup()


def porte_remy(x, y, taille, nombre_immeubles):
    penup()
    goto(x, y)
    setheading(0)
    color("black", "red")
    pensize(2)
    pendown()
    begin_fill()
    for _ in range(2):
        forward(taille)
        left(90)
        forward(taille * 2)
        left(90)
    end_fill()
    penup()


# ==============================================================================
# TOITS ET DECOR
# ==============================================================================


def toit_triangle(x, y, largeur_immeuble):
    penup()
    goto(x, y)
    setheading(0)
    color("black", "red")
    pensize(2)
    pendown()
    begin_fill()
    for _ in range(3):
        forward(largeur_immeuble)
        left(120)
    end_fill()
    penup()

    rayon = largeur_immeuble / 10
    goto(x + (largeur_immeuble / 2), y + (largeur_immeuble / 4))
    setheading(0)
    color("black", "lightblue")
    pensize(1)
    pendown()
    begin_fill()
    circle(rayon)
    end_fill()
    penup()


def toit_plat(x, y, largeur_immeuble):
    penup()
    goto(x, y)
    setheading(0)
    color("black", "darkgray")
    pensize(2)
    pendown()
    begin_fill()
    for _ in range(2):
        forward(largeur_immeuble)
        left(90)
        forward(12)
        left(90)
    end_fill()
    penup()


def toit_arrondi(x, y, largeur_immeuble):
    penup()
    goto(x + largeur_immeuble, y)
    setheading(90)
    color("black", "darkorange")
    pensize(2)
    pendown()
    begin_fill()
    circle(largeur_immeuble / 2, 180)
    setheading(0)
    forward(largeur_immeuble)
    end_fill()
    penup()


def tracer_ciel_et_astre(largeur_ecran, hauteur_ecran, marge_cadre):
    est_nuit = random.choice([True, False])
    y_astro = (hauteur_ecran / 2) - marge_cadre - 80

    if est_nuit:
        bgcolor("midnightblue")
        x_astro = (largeur_ecran / 2) - marge_cadre - 100
        penup()
        goto(x_astro, y_astro)
        color("yellow", "yellow")
        pendown()
        begin_fill()
        circle(35)
        end_fill()
        penup()
    else:
        bgcolor("skyblue")
        x_astro = -(largeur_ecran / 2) + marge_cadre + 100
        penup()
        goto(x_astro, y_astro)
        color("gold", "gold")
        pendown()
        begin_fill()
        circle(40)
        end_fill()
        penup()


def rue_evan(
    x_depart,
    y_depart,
    marge_cadre,
    hauteur_rue,
    largeur_ecran,
    nombre_immeubles,
):
    largeur_rue = largeur_ecran - 2 * marge_cadre
    epaisseur_trait = 11 - nombre_immeubles

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


def tracer_contour_rectangle(x, y, largeur, hauteur, couleur_fond):
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


def tracer_immeubles(
    x_rue,
    y_rue,
    marge_cadre,
    hauteur_rue,
    largeur_ecran,
    hauteur_ecran,
    nombre_immeubles,
    liste_couleurs,
):
    largeur_rue = largeur_ecran - 2 * marge_cadre
    marge_extremite_rue = 20
    espace_entre_immeubles = 20

    largeur_immeuble = (
        largeur_rue
        - 2 * marge_extremite_rue
        - (nombre_immeubles - 1) * espace_entre_immeubles
    ) / nombre_immeubles
    hauteur_toit = 0.866 * largeur_immeuble
    hauteur_dispo = (
        (hauteur_ecran / 2 - marge_cadre)
        - (y_rue + hauteur_rue)
        - hauteur_toit
        - 10
    )

    taille = largeur_immeuble / 5

    hauteur_etage_calculee = hauteur_dispo / nombre_immeubles
    hauteur_etage = max(2.5 * taille, hauteur_etage_calculee)

    if (hauteur_etage * nombre_immeubles) > hauteur_dispo:
        hauteur_etage = hauteur_dispo / nombre_immeubles
        taille = hauteur_etage / 2.5

    marge_interne_f = (largeur_immeuble - 3 * taille) / 4

    x_immeuble = x_rue + marge_extremite_rue
    y_immeuble = y_rue + hauteur_rue

    portes_dispo = [porte_evan, porte_loris, porte_remy]
    fenetres_dispo = [fenetre_evan, fenetre_loris, fenetre_remy]
    toits_dispo = [toit_triangle, toit_plat, toit_arrondi]

    for i in range(nombre_immeubles):
        nombre_niveaux = random.randint(1, nombre_immeubles)
        position_porte = random.randint(1, 3)

        couleur_bat = liste_couleurs[i]
        fonction_porte = random.choice(portes_dispo)

        for niveau in range(nombre_niveaux):
            y_niveau = y_immeuble + (niveau * hauteur_etage)
            tracer_contour_rectangle(
                x_immeuble, y_niveau, largeur_immeuble, hauteur_etage, couleur_bat
            )

            for emplacement in range(1, 4):
                x_elem = (
                    x_immeuble
                    + emplacement * marge_interne_f
                    + (emplacement - 1) * taille
                )

                if niveau == 0:
                    if emplacement == position_porte:
                        fonction_porte(
                            x_elem, y_niveau, taille, nombre_immeubles
                        )
                    else:
                        y_elem = y_niveau + (hauteur_etage - taille) / 2
                        fonction_fenetre = random.choice(fenetres_dispo)
                        fonction_fenetre(
                            x_elem, y_elem, taille, nombre_immeubles
                        )
                else:
                    y_elem = y_niveau + (hauteur_etage - taille) / 2
                    fonction_fenetre = random.choice(fenetres_dispo)
                    fonction_fenetre(x_elem, y_elem, taille, nombre_immeubles)

        y_sommet = y_immeuble + (nombre_niveaux * hauteur_etage)

        fonction_toit = random.choice(toits_dispo)
        fonction_toit(x_immeuble, y_sommet, largeur_immeuble)

        x_immeuble += largeur_immeuble + espace_entre_immeubles


# ==============================================================================
# BOUCLE PRINCIPALE
# ==============================================================================

marge_cadre = 30
hauteur_rue = 60

while True:
    largeur_ecran = window_width()
    hauteur_ecran = window_height()

    x_depart = -largeur_ecran / 2 + marge_cadre
    y_depart = -hauteur_ecran / 2 + marge_cadre

    nombre_immeubles = random.randint(3, 10)

    # Tirage au sort des couleurs au debut
    couleurs_immeubles = []
    for _ in range(nombre_immeubles):
        r = random.randint(50, 240)
        g = random.randint(50, 240)
        b = random.randint(50, 240)
        couleurs_immeubles.append((r, g, b))

    tracer_ciel_et_astre(largeur_ecran, hauteur_ecran, marge_cadre)
    rue_evan(
        x_depart,
        y_depart,
        marge_cadre,
        hauteur_rue,
        largeur_ecran,
        nombre_immeubles,
    )
    tracer_immeubles(
        x_depart,
        y_depart,
        marge_cadre,
        hauteur_rue,
        largeur_ecran,
        hauteur_ecran,
        nombre_immeubles,
        couleurs_immeubles,
    )
    update()
    time.sleep(temps_pause)
    clear()


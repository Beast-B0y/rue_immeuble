from turtle import *

# ==============================================================================
# FONCTIONS INDIVIDUELLES DES ÉLÉMENTS (MODULE EVAN)
# ==============================================================================

def fenetre_evan(x, y, i, nb_imm):
    """
    Dessine une fenêtre carrée de côté i avec croisillons.
    - x, y : Coin inférieur gauche de la fenêtre
    - i : Taille du côté de la fenêtre (l_elem)
    - nb_imm : Nombre d'immeubles dans la rue
    """
    penup()
    goto(x, y)
    setheading(0) 
    # Contour et Remplissage
    pensize(11-nb_imm)
    color("black", "lightblue")
    pendown()
    begin_fill()
    for _ in range(4):
        forward(i)
        left(90)
    end_fill()
    # Croisillons intérieurs
    color("brown")
    # Ligne verticale
    penup()
    goto(x + i / 2, y)
    pensize(0.75 * (11 - nb_imm))
    setheading(90)
    pendown()
    forward(i)
    # Ligne horizontale
    penup()
    goto(x, y + i / 2)
    setheading(0)
    pendown()
    forward(i)
    penup()


def porte_evan(x, y, i, nb_imm):
    """
    Dessine la porte d'Evan :
    - x, y : Coin inférieur gauche de la porte
    - i : Largeur élémentaire de la porte (l_elem)
    - nb_imm : Nombre d'immeubles dans la rue
    """
    penup()
    goto(x, y)
    setheading(0)
    # Contour et corps de la porte (cadre gris)
    color("black", "grey")
    pensize(11 - nb_imm)
    pendown()
    begin_fill()
    for _ in range(2):
        forward(i)
        left(90)
        forward(i * 2)
        left(90)
    end_fill()
    # Vitre en haut de la porte
    penup()
    goto(x + i * 0.1, y + i)
    pensize(0.5 * (11 - nb_imm))
    setheading(0)
    color("black", "lightblue")
    pendown()
    begin_fill()
    for _ in range(4):
        forward(i * 0.8)
        left(90)
    end_fill()
    # Poignée de porte
    penup()
    goto(x + i * 0.1, y + i * 0.8)
    setheading(0)
    color("black")
    pensize(0.5 * (11 - nb_imm))
    pendown()
    forward(i * 0.2)
    penup()


def toit(x, y, e, nb_imm):
    """
    Dessine un toit triangulaire sans débordement :
    - x, y : Coin supérieur gauche du dernier étage de l'immeuble
    - e : Largeur exacte de l'immeuble (la base du toit fait e)
    - nb_imm : Nombre d'immeubles dans la rue
    """
    penup()
    goto(x, y)  # Départ exact au coin supérieur gauche
    setheading(0)
    color("black", "red")
    pensize(11-nb_imm)
    pendown()
    begin_fill()
    for _ in range(3):
        forward(e)  # Longueur égale à la largeur de l'immeuble
        left(120)
    end_fill()
    penup()


def fenetre_toit(x, y, e, nb_imm):
    """
    Dessine la lucarne ronde centrée dans le toit :
    - x, y : Coin supérieur gauche du dernier étage de l'immeuble
    - e : Largeur de l'immeuble
    - nb_imm : Nombre d'immeubles dans la rue
    """
    rayon = e / 10
    penup()
    # Placement au centre horizontal du toit
    goto(x + (e / 2), y + (e / 4))
    setheading(0)
    color("black", "lightblue")
    pensize(0.5*(11-nb_imm))
    pendown()
    begin_fill()
    circle(rayon)
    end_fill()
    penup()

def rue_evan(x, y, a, b):       
    """
    Dessine une rue avec des immeubles.
    - x, y : Coin inférieur gauche de la rue
    - a : marge avec le bord de l'ecran(longueur de la rue)
    - b : marge avec le bord de l'ecran(largeur de la rue)
    """
    penup()
    goto(x, y)
    setheading(0)
    color("black", "grey")
    pendown()
    begin_fill()
    for _ in range(2):
        forward(a)
        left(90)
        forward(b)  # Hauteur de la rue
        left(90)
    end_fill()


## TESTS DES FONCTIONS INDIVIDUELLES    
fenetre_evan(-150, 0, 100, 10)
porte_evan(-50, 0, 50, 10)
toit(50, 0, 120, 7)
fenetre_toit(50, 0, 120, 7)


def rue_evan(x, y, a, b):       
    """
    Dessine une rue avec deux voies adaptées à la taille de l'écran.
    - x, y : Coin inférieur gauche de la rue
    - a : Marge avec le bord droit
    - b : Hauteur totale de la rue
    """
    longueur = (window_width() / 2 - a) - x
    
    # 1. Fond de la rue
    penup()
    goto(x, y)
    setheading(0)
    color("black", "grey")
    pendown()
    begin_fill()
    for _ in range(2):
        forward(longueur)
        left(90)
        forward(b)
        left(90)
    end_fill()
    # 2. Ligne discontinue blanche
    penup()
    goto(x, y + b / 2)  # Positionnement au milieu de la hauteur
    color("yellow")
    pensize(2)
    # Trace des pointillés jusqu'au bout de la rue
    pos_x = x
    while pos_x < (x + longueur):
        pendown()
        forward(15)  # Trait
        penup()
        forward(10)  # Espace
        pos_x += 25


# appel rue (adapté à la taille de l'écran)
a = 20
b = 60
x_depart = -window_width() / 2 + a
y_depart = -window_height() / 2 + a

rue_evan(x_depart, y_depart, a, b)

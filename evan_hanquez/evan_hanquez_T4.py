from turtle import *

# ==============================================================================
# FONCTIONS INDIVIDUELLES DES ÉLÉMENTS (MODULE EVAN)
# ==============================================================================

def fenetre_evan(x, y, i):
    """
    Dessine une fenêtre carrée de côté i avec croisillons.
    - x, y : Coin inférieur gauche de la fenêtre
    - i : Taille du côté de la fenêtre (l_elem)
    """
    penup()
    goto(x, y)
    setheading(0)
    
    # Contour et Remplissage
    pensize(2)
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


def porte_evan(x, y, i):
    """
    Dessine la porte d'Evan :
    - x, y : Coin inférieur gauche de la porte
    - i : Largeur élémentaire de la porte (l_elem)
    """
    j = i / 5  # Épaisseur dynamique de l'encadrement de l'imposte

    penup()
    goto(x, y)
    setheading(0)
    
    # Contour et corps de la porte (cadre gris)
    color("black", "grey")
    pensize(2)
    pendown()
    begin_fill()
    for _ in range(2):
        forward(i)
        left(90)
        forward(i * 2)
        left(90)
    end_fill()

    # Vitre / Imposte en haut de la porte
    penup()
    goto(x + j / 2, y + i)
    setheading(0)
    color("black", "lightblue")
    pendown()
    begin_fill()
    for _ in range(4):
        forward(i - j)
        left(90)
    end_fill()

    # Poignée de porte
    penup()
    goto(x + i * 0.1, y + i * 0.8)
    setheading(0)
    color("black")
    pensize(2)
    pendown()
    forward(i * 0.2)
    penup()


def toit(x, y, e):
    """
    Dessine un toit triangulaire sans débordement :
    - x, y : Coin supérieur gauche du dernier étage de l'immeuble
    - e : Largeur exacte de l'immeuble (la base du toit fait e)
    """
    penup()
    goto(x, y)  # Départ exact au coin supérieur gauche
    setheading(0)
    
    color("black", "red")
    pensize(3)
    pendown()
    begin_fill()
    for _ in range(3):
        forward(e)  # Longueur égale à la largeur de l'immeuble
        left(120)
    end_fill()
    penup()


def fenetre_toit(x, y, e):
    """
    Dessine la lucarne ronde centrée dans le toit :
    - x, y : Coin supérieur gauche du dernier étage de l'immeuble
    - e : Largeur de l'immeuble
    """
    rayon = e / 10
    
    penup()
    # Placement au centre horizontal du toit
    goto(x + (e / 2), y + (e / 4))
    setheading(0)
    
    color("black", "lightblue")
    pensize(1)
    pendown()
    begin_fill()
    circle(rayon)
    end_fill()
    penup()
    
fenetre_evan(-150, 0, 50)
porte_evan(-50, 0, 40)
toit(50, 0, 120)
fenetre_toit(50, 0, 120)
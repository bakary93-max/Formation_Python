import turtle
""""
forward(n) pour avancer de n pixels
backward pour reculer
right(90) tourner à droite avec un angle de 90°
left(45) tourner à gauche avec un angle de 45°
"""
def escalier(taille, nb):
    t = turtle.Turtle()
    # deplacement en avant de 100 pixel
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)

    turtle.done()

def carre(taille):
    t = turtle.Turtle()
    # deplacement en avant de 100 pixel
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)

    turtle.done()

def carres(taille_depart, nb):
    t = turtle.Turtle()
    # deplacement en avant de 100 pixel
    for i in range(0, nb):
        taille = taille_depart * (i+1)
        carre(taille)
""""
forward(n) pour avancer de n pixels
backward pour reculer
right(90) tourner à droite avec un angle de 90°
left(45) tourner à gauche avec un angle de 45°
"""
import turtle
t = turtle.Turtle()
# deplacement en avant de 100 pixels
t.forward(100)
t.right(30)
t.forward(100)



for i in range(0, 5):
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
t.forward(30)
turtle.done()

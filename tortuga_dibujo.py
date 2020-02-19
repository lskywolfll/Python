import turtle
recuadro = turtle.Screen()
tortugita = turtle.Turtle()

# Dibujo por movimientos
# tortugita.forward(50)
# tortugita.left(90)

def lineaCuadrada(adelante,movimiento, veces):
    for i in range(1,veces + 1):
        tortugita.forward(adelante)
        tortugita.left(movimiento)
        if i == veces + 1:
            turtle.mainloop()

lineaCuadrada(50,90,4)
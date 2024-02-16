from turtle import *
from math import *

import pygame

speed(0)
bgcolor("black")
goto(0, -40)

# Función para dibujar el girasol
def dibujar_girasol():
    for i in range(15):
        for j in range(18):
            color('#FFA216')
            rt(90)
            circle(150-j*6, 90)
            lt(90)
            circle(150-j*6, 90)
            rt(180)
        circle(40, 24)

    color('black')
    shape('circle')
    shapesize(0.5)
    fillcolor('#8B4513')
    golden_angle = 137.508

    phi = golden_angle*(pi/180)

    for i in range(110):
        r = 4*sqrt(i)
        theta = i*phi
        x = r*cos(theta)
        y = r*sin(theta)
        penup()
        goto(x, y)
        setheading(i*golden_angle)
        pendown()
        stamp()

# Dibujar el girasol
dibujar_girasol()
pygame.time.wait(1000)

def mostrar_mensaje(mensaje, indice_mensaje):
    penup()
    # Borrar mensaje anterior
    if indice_mensaje > 0:
        clear()
    goto(-50,-20)
    setheading(0)
    color("white")
    write(mensaje, font=("Arial", 30, "bold"))
    pendown()
def mostrar_mensajes(mensajes):
    indice_mensaje = 0
    for mensaje in mensajes:
        mostrar_mensaje(mensaje, indice_mensaje)
        indice_mensaje += 1
        # Espera un segundo entre mensajes
        pygame.time.wait(1500)

cadena = "Feliz San Valentín! Me gustaría seguir conociéndote y descubrir más sobre ti"
mensajes = cadena.split(" ")
ghost = "\U0001F47B"
mensajes[len(mensajes)-1] += f' {ghost}'

mostrar_mensajes(mensajes)
hideturtle()

done()

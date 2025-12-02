import pygame
from ayudas import *
from boton import *

class Botonjugar:
    texto = 'press SPACE to PAUSE'
    letra = letra_pixel
    color = limon
    x = 100
    y = 50
    size = 40
    parpadear = False
    parpadeo = 0
    tiempo = 0

class salir:
    texto = 'SALIR'
    letra = letra_pixel
    color = limon
    x = 100
    y = 50
    size = 40
    parpadear = False
    parpadeo = 0
    tiempo = 0

class fondoInicio:
    fondo = pygame.image.load("./imagenes/inicio.jpg")
    imagen = pygame.transform.scale(fondo,(ANCHO,ALTO))
    ancho, alto = imagen.get_size()
    posicion = 0

def verVentana1():
    (fondoInicio)
    ponerTexto(Botonjugar)
    ponerTexto(salir)
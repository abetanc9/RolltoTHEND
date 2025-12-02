import pygame
from ayudas import *
from boton import *

# RUTA DE IMAGEN
IMG_INICIO = "./imagenes/inicio.jpg"

# RUTA DE FUENTE PIXEL
FUENTE_PIXEL = "./fonts/VT323-Regular.ttf"

def start_screen():
    # cargar imagen
    fondo = pygame.image.load(IMG_INICIO).convert()
    fondo = pygame.transform.scale(fondo, ventana.get_size())
    amusement.play()

    # crear botones
    boton_jugar = Boton(
        texto="JUGAR",
        x=800,
        y=925,
        w=250,
        h=80,
        font=FUENTE_PIXEL,
        font_size=50,
        color_base=(26, 62, 62),
        color_hover=(40, 90, 90),
        color_texto=(240, 220, 170)
    )

    boton_salir = Boton(
        texto="SALIR",
        x=1100,
        y=925,
        w=250,
        h=80,
        font=FUENTE_PIXEL,
        font_size=50,
        color_base=(26, 62, 62),
        color_hover=(40, 90, 90),
        color_texto=(240, 220, 170)
    )

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.click():
                    print("Iniciar juego")
                    return "JUGAR"

                if boton_salir.click():
                    pygame.quit()
                    exit()

        ventana.blit(fondo, (0, 0))

        boton_jugar.draw()
        boton_salir.draw()

        pygame.display.update()

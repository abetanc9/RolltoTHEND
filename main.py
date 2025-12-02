import pygame
from start_screen import *
from ayudas import *

pygame.init()

def main():
    opcion = start_screen()

    if opcion == "JUGAR":
        print("Aquí irá tu juego real")
        # TODO: llamar a ventana principal del juego

if __name__ == "__main__":
    main()


# import pygame, sys
# from ayudas import *
# from ventana1 import *


# # -----------------------------
# #   ZONA DE FUNCIONES
# # -----------------------------

# def inicio():
#     """
#     Pantalla inicial temporal para evitar el error.
#     Puedes personalizarla luego.
#     """

#     # Fondo sólido (puedes cambiarlo)
#     ventana.fill((30, 30, 30))

#     # Texto en pantalla
#     font = pygame.font.SysFont('Arial', 50)
#     texto = font.render("perro hpta", True, (255, 255, 255))

#     ventana.blit(
#         texto, 
#         (ANCHO // 2 - texto.get_width() // 2,
#          ALTO // 2 - texto.get_height() // 2)
#     )


# # -----------------------------
# #   BUCLE PRINCIPAL DEL JUEGO
# # -----------------------------

# if __name__ == '__main__':

#     while True:

#         Ayudas.EVENTOS = pygame.event.get()

#         for evento in Ayudas.EVENTOS:

#             if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
#                 pygame.quit()
#                 sys.exit()

#             if evento.type == pygame.KEYUP:
#                 if evento.key == pygame.K_RIGHT:
#                     Ayudas.ACCION = 'pausado_derecha'

#                 if evento.key == pygame.K_LEFT:
#                     Ayudas.ACCION = 'pausado_izquierda'

#             if evento.type == pygame.KEYDOWN:
#                 if evento.key == pygame.K_RSHIFT:
#                     Ayudas.ACCION = 'saltando_derecha'
#                 if evento.key == pygame.K_LSHIFT:
#                     Ayudas.ACCION = 'saltando_izquierda'

#         ventana.fill(blanco)

#         verVentana1()

#         # Ejecuta la pantalla actual
#         eval(Ayudas.actual + '()')

#         pygame.display.update()
#         RELOJ.tick(FPS)
import pygame
from ayudas import ventana

class Boton:
    def __init__(self, texto, x, y, w, h, font, font_size, color_base, color_hover, color_texto):
        self.texto = texto
        self.rect = pygame.Rect(x, y, w, h)
        self.color_base = color_base
        self.color_hover = color_hover
        self.color_texto = color_texto
        self.font = pygame.font.Font(font, font_size)

    def draw(self):
        mouse = pygame.mouse.get_pos()
        color = self.color_hover if self.rect.collidepoint(mouse) else self.color_base
        pygame.draw.rect(ventana, color, self.rect)

        texto_render = self.font.render(self.texto, True, self.color_texto)
        ventana.blit(
            texto_render,
            (
                self.rect.centerx - texto_render.get_width() // 2,
                self.rect.centery - texto_render.get_height() // 2
            )
        )

    def click(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
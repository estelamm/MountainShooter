#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')  # imagem menu
        self.rect = self.surf.get_rect(left=0, top=0)  # retangulo

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')  # carregar musica
        pygame.mixer_music.play(-1)  # tocar musica ((-1) = tocar em repeat)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # desenhar imagem no retangulo
            self.menu_text(50, "Mountain", COLOR_WHITE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_WHITE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

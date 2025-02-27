#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png') #imagem menu
        self.rect = self.surf.get_rect(left=0, top=0) #retangulo

    def run(self, ):
        self.window.blit(source=self.surf, dest=self.rect) #desenhar imagem no retangulo
        pygame.display.flip()
        pass

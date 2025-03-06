#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name: str, position:tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod  #classe abstrata implica que todos os metodos dentro dela serão implementados pelos seus filhos
    def move(self, ):
        pass

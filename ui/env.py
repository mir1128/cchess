# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit
from log import logger

class Env(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("cchess")
        self.__screen = pygame.display.set_mode((720, 800), 0, 32)

    def loadImage(self, path):
        return pygame.image.load(path).convert()

    def run(self, ui):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONUP:
                logger.logger.info('MOUSEBUTTONUP: %s', str(pygame.mouse.get_pos()))


        pygame.display.update()




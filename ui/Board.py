# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit
from log import logger
import ui


class Board(ui):
    __ROW = 10
    __COL = 9

    def __init__(self, mode=0):
        pygame.init()
        pygame.display.set_caption("cchess")

        if mode == 1:
            self.__board = [[1, 2, 3, 4, 7, 4, 3, 2, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 5, 0, 0, 0, 0, 0, 5, 0],
                            [6, 0, 6, 0, 6, 0, 6, 0, 6],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [16, 0, 16, 0, 16, 0, 16, 0, 16],
                            [0, 15, 0, 0, 0, 0, 0, 15, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [11, 12, 13, 14, 17, 14, 13, 12, 11]]
        elif mode == 0:
            self.__board = [[11, 12, 13, 14, 17, 14, 13, 12, 11],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 15, 0, 0, 0, 0, 0, 15, 0],
                            [16, 0, 16, 0, 16, 0, 16, 0, 16],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [6, 0, 6, 0, 6, 0, 6, 0, 6],
                            [0, 5, 0, 0, 0, 0, 0, 5, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 2, 3, 4, 7, 4, 3, 2, 1]]

        self.__chess_file_mapping = {(1, 'red_rook'), (2, 'red_knight'), (3, 'red_elephant'), (4, 'red_mandarin'),
                                     (5, 'red_cannon'), (6, 'red_pawn'), (7, 'red_king'),
                                     (11, 'black_rook'), (12, 'black_knight'), (13, 'black_elephant'),
                                     (14, 'black_mandarin'), (15, 'black_cannon'), (16, 'black_pawn'),
                                     (17, 'black_king')};

        self.__background_image_filename = '../images/boardchess.jpg'
        self.__chess_img_mapping = {}

        self.__screen = pygame.display.set_mode((720, 800), 0, 32)
        self.__background = pygame.image.load(self.__background_image_filename).convert()
        for (key, name) in self.__chess_file_mapping:
            self.__chess_img_mapping[key] = pygame.image.load('../images/' + name + '.jpg').convert()

    def display(self, board):
        self.__board = board
        self.refresh()

    def refresh(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONUP:
                logger.logger.info('MOUSEBUTTONUP: %s', str(pygame.mouse.get_pos()))

        self.__screen.blit(self.__background, (0, 0))
        for row in range(Board.__ROW):
            for col in range(Board.__COL):
                if self.__board[row][col] != 0:
                    self.__screen.blit(self.__chess_img_mapping[self.__board[row][col]], (col * 80, row * 80))

        pygame.display.update()

    def move(self, c, src, dst):
        chess = []


if __name__ == '__main__':
    b = Board(0)

    while True:
        b.refresh()

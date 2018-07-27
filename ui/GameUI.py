# -*- coding: utf-8 -*-

from sys import exit
from pygame.locals import *
from log.logger import logger
import pygame


class GameUI(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("cchess")
        self.__screen = pygame.display.set_mode((720, 800), 0, 32)
        self.__background = pygame.image.load('../images/boardchess.jpg').convert()

        self.__chess_file_mapping = {(1, 'red_rook'), (2, 'red_knight'), (3, 'red_elephant'), (4, 'red_mandarin'),
                                     (5, 'red_cannon'), (6, 'red_pawn'), (7, 'red_king'),
                                     (11, 'black_rook'), (12, 'black_knight'), (13, 'black_elephant'),
                                     (14, 'black_mandarin'), (15, 'black_cannon'), (16, 'black_pawn'),
                                     (17, 'black_king')}
        self.__chess_img_mapping = {}
        for (key, name) in self.__chess_file_mapping:
            self.__chess_img_mapping[key] = pygame.image.load('../images/' + name + '.jpg')

    def loadImage(self, path):
        return pygame.image.load(path).convert()

    def putPiece(self, piece, position):
        row, col = position
        self.__screen.blit(self.__chess_img_mapping[piece], (col * 80, row * 80))

    def run(self):

        board = Board.Board()

        is_piece_picked = False
        piece_src_position = None
        which_piece_is_picked = None

        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    button_up_pos = pygame.mouse.get_pos()
                    which_piece_is_picked = self.getPieceByPosition(board, button_up_pos)
                    if not is_piece_picked:
                        is_piece_picked = True
                        piece_src_position = button_up_pos
                    else:
                        src = self.toBoardPos(piece_src_position)
                        dst = self.toBoardPos(button_up_pos)
                        isValid, isFinished = board.move(which_piece_is_picked, src, dst)
                        is_piece_picked = False
                        piece_src_position = None
                        if not isValid:
                            logger.info('invalid move src %s, dst %s', str(src), str(dst))
                        if isFinished:
                            


                if event.type == QUIT:
                    exit()

                self.__screen.blit(self.__background, (0, 0))
                board.putPieces(self)
                pygame.display.update()

    def getPieceByPosition(self, board,  button_up_pos):
        row, col = self.toBoardPos(button_up_pos)
        return board.get(row, col)

    def toBoardPos(self, pos):
        x, y = pos
        return y/80, x/80

if __name__ == '__main__':
    from ui import Board

    e = GameUI()
    e.run()

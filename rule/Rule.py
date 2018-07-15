# -*- coding: utf-8 -*-

from log import logger
import constants


class Rule(object):
    """
        check(self, src, dst, board)
        return (boolean, boolean) Returns 2 boolean values, the first indicates whether the step is legal, and the second indicates whether the game is over
    """

    def __init__(self):
        pass

    def check(self, src, dst, board):
        row_src, col_src = src
        row_dst, row_dst = dst

        if (not 0 <= row_src <= 10) or (not 0 <= col_src <= 9) or (not 0 <= row_dst <= 10) or (not 0 <= row_dst <= 9):
            logger.logger.error("invalid pos src %s, dst %s, board: %s", str(src), str(dst), str(board))
            raise NameError("index out of bound")

        return True, False

    def isOver(self, board):
        return not (1 in [item for sublist in board for item in sublist] and 11 in [item for sublist in board for item in sublist])

    def redWin(self, board):
        return 11 not in [item for sublist in board for item in sublist]

    def blackWin(self, board):
        return 1 not in [item for sublist in board for item in sublist]

    def isOverAfterStep(self, dst, board):
        row_dst, row_dst = dst
        return board[row_dst][row_dst] == constants.RED_KING or board[row_dst][row_dst] == constants.BLACK_KING

    def isRedWinAfterStep(self, dst, board):
        row_dst, row_dst = dst
        return board[row_dst][row_dst] == constants.BLACK_KING

    def isBlackWinAfterStep(self, dst, board):
        row_dst, row_dst = dst
        return board[row_dst][row_dst] == constants.RED_KING

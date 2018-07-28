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
        row_dst, col_dst = dst

        if (not 0 <= row_src <= 10) or (not 0 <= col_src <= 9) or (not 0 <= row_dst <= 10) or (not 0 <= row_dst <= 9):
            logger.logger.error("invalid pos src %s, dst %s, board: %s", str(src), str(dst), str(board))
            raise NameError("index out of bound")

        if board[row_src, col_src] == 0:
            logger.logger.error("there is no chess at src: %s", str(src))
            return False, False

        if board[row_src, col_src] < constants.BLACK_RED_LINE and board[row_dst, col_dst] != 0 and  board[row_dst, col_dst] < constants.BLACK_RED_LINE:
            logger.logger.error("can not eat same side piece src: %s value %d, dst %s value %d", str(src), board[row_src, col_src], str(dst), board[row_dst, col_dst])
            return False, False

        if board[row_src, col_src] > constants.BLACK_RED_LINE and board[row_dst, col_dst] > constants.BLACK_RED_LINE:
            logger.logger.error("can not eat same side piece src: %s value %d, dst %s value %d", str(src), board[row_src, col_src], str(dst), board[row_dst, col_dst])
            return False, False

        return True, False

    def isOver(self, board):
        return not (1 in [item for sublist in board for item in sublist] and 11 in [item for sublist in board for item in sublist])

    def redWin(self, board):
        return 11 not in [item for sublist in board for item in sublist]

    def blackWin(self, board):
        return 1 not in [item for sublist in board for item in sublist]

    def isOverAfterStep(self, dst, board):
        row_dst, col_dst = dst
        return board[row_dst, col_dst] == constants.RED_KING or board[row_dst, col_dst] == constants.BLACK_KING

    def isRedWinAfterStep(self, dst, board):
        row_dst, col_dst = dst
        return board[row_dst, col_dst] == constants.BLACK_KING

    def isBlackWinAfterStep(self, dst, board):
        row_dst, col_dst = dst
        return board[row_dst, col_dst] == constants.RED_KING

    def isSameSide(self, src, dst, board):
        row_src, col_src = src
        row_dst, col_dst = dst

        if board[row_src, col_src] < constants.BLACK_RED_LINE and board[row_dst, col_dst] < constants.BLACK_RED_LINE and board[row_src, col_src] != 0 and board[row_dst, col_dst] != 0:
            return True
        if board[row_src, col_src] > constants.BLACK_RED_LINE and board[row_dst, col_dst] > constants.BLACK_RED_LINE:
            return True
        return False

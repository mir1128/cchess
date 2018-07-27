# -*- coding: utf-8 -*-

import constants


class TurnRule(object):

    def __init__(self):
        self.whos_turn = constants.RED_TURN

    def check(self, src, board):
        row_src, col_src = src
        if board[row_src, col_src] < constants.BLACK_RED_LINE and board[row_src, col_src] !=0 and self.whos_turn == constants.RED_TURN:
            return True
        if board[row_src, col_src] > constants.BLACK_RED_LINE and self.whos_turn == constants.BLACK_TRUN:
            return True
        return False

    def nextTurn(self):
        if self.whos_turn == constants.RED_TURN:
            self.whos_turn = constants.BLACK_TRUN
        else:
            self.whos_turn = constants.RED_TURN



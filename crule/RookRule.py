# -*- coding: utf-8 -*-

from Rule import Rule
import constants


class RookRule(Rule):

    def __init__(self):
        super(RookRule, self).__init__()

    def check(self, src, dst, board):
        row_src, col_src = src
        row_dst, col_dst = dst

        if (board[row_src, col_src] != constants.BLACK_ROOK) and (board[row_src, col_src] != constants.RED_ROOK):
            return False, False

        # 起点和终点不在一条线上
        if (row_src != row_dst) and (col_src != col_dst):
            return False, False

        # 在同一行
        if row_src == row_dst:
            if abs(col_src - col_dst) == 1:
                return True, super(RookRule, self).isOverAfterStep(dst, board)
            if any(v != 0 for v in board[row_src, min(col_src, col_dst) + 1: max(col_src, col_dst)].tolist()):
                return False, False

        # 在同一列
        if col_src == col_dst:
            if abs(row_src - row_dst) == 1:
                return True, super(RookRule, self).isOverAfterStep(dst, board)

            if any(v != 0 for v in board[min(row_src, row_dst) + 1: max(row_src, row_dst), col_src].tolist()):
                return False, False

        # 目标位置没有棋子
        if board[row_src, col_src] < constants.BLACK_RED_LINE and board[row_dst, col_dst] == 0:
            return True, False

        # 红子吃掉黑子
        if board[row_src, col_src] < constants.BLACK_RED_LINE < board[row_dst, col_dst]:
            return True, super(RookRule, self).isOverAfterStep(dst, board)

        # 黑子吃掉红子
        if board[row_src, col_src] > constants.BLACK_RED_LINE > board[row_dst, col_dst]:
            return True, super(RookRule, self).isOverAfterStep(dst, board)

        return True, False


if __name__ == '__main__':
    import numpy as np

    r = RookRule()
    s1 = np.array([[1, 2, 3, 4, 7, 4, 3, 2, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 5, 0, 0, 0, 0, 0, 5, 0],
                   [6, 0, 6, 0, 6, 0, 6, 0, 6],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [16, 0, 16, 0, 16, 0, 16, 0, 16],
                   [0, 15, 0, 0, 0, 0, 0, 15, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [11, 12, 13, 14, 17, 14, 13, 12, 11]])

    try:
        print(r.check((0, 0), (3, 0), s1))
    except NameError, e:
        print(e.message)

    s2 = np.array([[1, 2, 3, 4, 7, 4, 3, 2, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 5, 0, 0, 0, 0, 0, 5, 0],
                   [0, 0, 6, 0, 6, 0, 6, 0, 6],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [16, 0, 16, 0, 16, 0, 16, 0, 16],
                   [0, 15, 0, 0, 0, 0, 0, 15, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [11, 12, 13, 14, 17, 14, 13, 12, 11]])

    try:
        print(r.check((0, 0), (6, 0), s2))
    except NameError, e:
        print(e.message)

# -*- coding: utf-8 -*-

from Rule import Rule
import constants


class KinghtRule(Rule):
    def __init__(self):
        super(KinghtRule, self).__init__()

    def check(self, src, dst, board):
        super(KinghtRule, self).check(src, dst, board)

        row_src, col_src = src
        row_dst, col_dst = dst

        # 走日
        if not ((abs(row_src - row_dst) == 2 and abs(col_src - col_dst) == 1) or (abs(row_src - row_dst) == 1 and abs(col_src - col_dst) == 2)):
            return False, False

        if row_src - row_dst == 2 and board[row_src - 1, col_src] != 0:
            return False, False

        if row_dst - row_src == 2 and board[row_src + 1, col_src] != 0:
            return False, False

        if col_src - col_dst == 2 and board[row_src, col_src - 1] != 0:
            return False, False

        if col_dst - col_src == 2 and board[row_src, col_src + 1] != 0:
            return False, False

        # 红子吃掉黑子
        if board[row_src, col_src] < constants.BLACK_RED_LINE < board[row_dst, col_dst]:
            return True, super(KinghtRule, self).isOverAfterStep(dst, board)

        # 黑子吃掉红子
        if board[row_src, col_src] > constants.BLACK_RED_LINE > board[row_dst, col_dst]:
            return True, super(KinghtRule, self).isOverAfterStep(dst, board)

        return True, False


if __name__ == '__main__':
    import numpy as np

    r = KinghtRule()
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
        print(r.check((0, 1), (2, 2), s1))
    except NameError, e:
        print(e.message)

    try:
        print(r.check((0, 1), (1, 2), s1))
    except NameError, e:
        print(e.message)

    try:
        print(r.check((0, 1), (1, 3), s1))
    except NameError, e:
        print(e.message)

    try:
        print(r.check((0, 1), (2, 0), s1))
    except NameError, e:
        print(e.message)
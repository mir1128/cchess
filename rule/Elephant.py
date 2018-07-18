# -*- coding: utf-8 -*-

from Rule import Rule
import constants


class ElephantRule(Rule):
    def __init__(self):
        super(ElephantRule, self).__init__()

    def check(self, src, dst, board):
        super(ElephantRule, self).check(src, dst, board)

        row_src, col_src = src
        row_dst, col_dst = dst

        if (board[row_src, col_src] != constants.BLACK_ELEPHANT) and (board[row_src, col_src] != constants.RED_ELEPHANT):
            return False, False

        if not (abs(row_src - row_dst) == 2 and abs(col_src - col_dst) == 2):
            return False, False

        lo = [(0, 2), (0, 6), (2, 0), (2, 4), (2, 8), (4, 2), (4, 6)]
        hi = [(5, 2), (5, 6), (7, 0), (7, 4), (7, 8), (9, 2), (9, 6)]

        if (src not in lo) and (src not in hi):
            return False, False

        if (dst not in lo) and (dst not in hi):
            return False, False

        if (src in lo and dst not in lo) or (src in hi and dst not in hi):
            return False, False

        # 红子吃掉黑子
        if board[row_src, col_src] < constants.BLACK_RED_LINE < board[row_dst, col_dst]:
            return True, super(ElephantRule, self).isOverAfterStep(dst, board)

        # 黑子吃掉红子
        if board[row_src, col_src] > constants.BLACK_RED_LINE > board[row_dst, col_dst]:
            return True, super(ElephantRule, self).isOverAfterStep(dst, board)

        return True, False


if __name__ == '__main__':
    import numpy as np

    r = ElephantRule()
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
        print(r.check((0, 2), (2, 0), s1))
    except NameError, e:
        print(e.message)

    try:
        print(r.check((0, 2), (2, 4), s1))
    except NameError, e:
        print(e.message)

    try:
        print(r.check((0, 2), (2, 5), s1))
    except NameError, e:
        print(e.message)

    try:
        print(r.check((9, 2), (7, 0), s1))
    except NameError, e:
        print(e.message)

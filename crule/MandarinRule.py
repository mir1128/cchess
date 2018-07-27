# -*- coding: utf-8 -*-

from Rule import Rule
import constants


class MandarinRule(Rule):
    def __init__(self):
        super(MandarinRule, self).__init__()

    def check(self, src, dst, board):
        row_src, col_src = src
        row_dst, col_dst = dst

        if (board[row_src, col_src] != constants.BLACK_MANDARIN) and (board[row_src, col_src] != constants.RED_MANDARIN):
            return False, False

        if not (abs(row_src - row_dst) == 1 and abs(col_src - col_dst) == 1):
            return False, False

        lo = [(0, 3), (0, 5), (1, 4), (2, 3), (2, 5)]
        hi = [(9, 3), (9, 5), (8, 4), (7, 4), (7, 5)]

        if (src not in lo) and (src not in hi):
            return False, False

        if (dst not in lo) and (dst not in hi):
            return False, False

        if (src in lo and dst not in lo) or (src in hi and dst not in hi):
            return False, False

        # 红子吃掉黑子
        if board[row_src, col_src] < constants.BLACK_RED_LINE < board[row_dst, col_dst]:
            return True, super(MandarinRule, self).isOverAfterStep(dst, board)

        # 黑子吃掉红子
        if board[row_src, col_src] > constants.BLACK_RED_LINE > board[row_dst, col_dst]:
            return True, super(MandarinRule, self).isOverAfterStep(dst, board)

        return True, False


if __name__ == '__main__':
    import numpy as np

    r = MandarinRule()
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
        print(r.check((0, 3), (1, 4), s1))
    except NameError, e:
        print(e.message)
        
    try:
        print(r.check((0, 3), (1, 2), s1))
    except NameError, e:
        print(e.message)
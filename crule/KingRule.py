# -*- coding: utf-8 -*-

from Rule import Rule
import constants


class KingRule(Rule):
    def __init__(self):
        super(KingRule, self).__init__()

    def check(self, src, dst, board):
        super(KingRule, self).check(src, dst, board)

        row_src, col_src = src
        row_dst, col_dst = dst

        if (board[row_src, col_src] != constants.BLACK_KING) and (board[row_src, col_src] != constants.RED_KING):
            return False, False

        lo = [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]
        hi = [(9, 3), (9, 4), (9, 5), (8, 3), (8, 4), (8, 5), (7, 3), (7, 4), (7, 5)]

        if (src in lo) and (dst in hi) and col_src == col_dst and all(v == 0 for v in board[row_src+1 : row_dst, col_src]):
            return True, True

        if (src in hi) and (dst in lo) and col_src == col_dst and all(v == 0 for v in board[row_dst+1: row_src, col_src]):
            return True, True

        if not ((abs(row_src - row_dst) == 1 and abs(col_src - col_dst) == 0) or (abs(row_src - row_dst) == 0 and abs(col_src - col_dst) == 1)) :
            return False, False

        if (src not in lo) and (src not in hi):
            return False, False

        if (dst not in lo) and (dst not in hi):
            return False, False

        if (src in lo and dst not in lo) or (src in hi and dst not in hi):
            return False, False

        return True, False


if __name__ == '__main__':
    import numpy as np

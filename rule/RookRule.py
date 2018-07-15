# -*- coding: utf-8 -*-

from Rule import Rule
import constants


class RookRule(Rule):

    def __init__(self):
        super(RookRule, self).__init__()

    def check(self, src, dst, board):
        super(RookRule, self).check(src, dst, board)

        row_src, col_src = src
        row_dst, col_dst = dst

        if (board[row_src][col_src] != constants.BLACK_ROOK) and (board[row_src][col_src] != constants.RED_ROOK):
            return False, False

        if (row_src != row_dst) and (col_src != col_dst):
            return False, False

        if row_src == row_dst:
            if any(v != 0 for v in board[row_src][col_src : col_dst]):
                return False, False

        if col_src == col_dst:
            if any(v != 0 for v in board[row_src : row_dst][col_src]):
                return False, False

        if board[row_src][col_src] < constants.BLACK_RED_LINE and board[row_dst][col_dst] > constants.BLACK_RED_LINE:
            return True, super(RookRule, self).isOverAfterStep(dst, board)

        return True, False

if __name__ == '__main__':
    r = RookRule()
    s1 = [[1, 2, 3, 4, 7, 4, 3, 2, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 5, 0, 0, 0, 0, 0, 5, 0],
         [6, 0, 6, 0, 6, 0, 6, 0, 6],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [16, 0, 16, 0, 16, 0, 16, 0, 16],
         [0, 15, 0, 0, 0, 0, 0, 15, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [11, 12, 13, 14, 17, 14, 13, 12, 11]]

    print(r.check((0, 0), (3, 0), s1))

    s2 = [[1, 2, 3, 4, 7, 4, 3, 2, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 5, 0, 0, 0, 0, 0, 5, 0],
          [0, 0, 6, 0, 6, 0, 6, 0, 6],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [16, 0, 16, 0, 16, 0, 16, 0, 16],
          [0, 15, 0, 0, 0, 0, 0, 15, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [11, 12, 13, 14, 17, 14, 13, 12, 11]]

    print(r.check((0, 0), (6, 0), s2))

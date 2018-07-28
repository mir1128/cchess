# -*- coding: utf-8 -*-

from TreeNode import TreeNode
from board.BoardExtend import BoardExtend
from log.logger import logger


class GameTree(object):
    def __init__(self):
        self.__root = None

    def compute(self, node, level):
        if level == 0:
            return

        board = node.getBoard()
        movements = board.nextPossibleMovements()

        if len(movements) == 0:
            logger.info("board.nextPossibleMovements return empty list.")
            return

        for mov in movements:
            row_src, col_src, row_dst, col_dst = mov

            board_copy = board.clone()
            board_copy.move(board_copy.get(row_src, col_src), (row_src, col_src), (row_dst, col_dst))
            child = TreeNode()
            child.setBoard(board_copy)
            node.addChild(child)

            next_level = level - 1
            self.compute(child, next_level)

    def buildTree(self, board, level):
        node = TreeNode()
        node.setBoard(board.clone())
        self.compute(node, level)

        return node


if __name__ == '__main__':
    board = BoardExtend()
    game_tree = GameTree()

    node = game_tree.buildTree(board, 2)
    node.format()



# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self):
        self.__children = []
        self.__board = None
        self.__score = 0

    def setBoard(self, board):
        self.__board = board
        return self

    def addChild(self, child):
        self.__children.append(child)
        return self

    def setScore(self, score):
        self.__score = score
        return self

    def getBoard(self):
        return self.__board

    def getScore(self):
        return self.__score

    def getChildren(self):
        return self.__children

    def output(self):
        return self.__board.output()

if __name__ == '__main__':
    print "hello world"

#!/usr/bin/env python
# -*- conding:utf-8 -*-
__author__ = 'unicoe'
__date__ = '2017/8/27'
__time__ = '22:41'


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        print board
        

s = Solution()

l1 = ['x','.','.','x']
l2 = ['.','.','.','x']
l3 = ['.','.','.','x']
l = [l1,l2,l3]

s.countBattleships(l)
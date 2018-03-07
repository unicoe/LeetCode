#!/usr/bin/env python
# -*- conding:utf-8 -*-
__author__ = 'unicoe'
__date__ = '2017/8/27'
__time__ = '14:12'


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vertical = 0
        horizontal = 0

        for i in xrange(len(moves)):
            if moves[i] == 'U':
                vertical += 1
            elif moves[i] == 'D':
                vertical -= 1
            elif moves[i] == 'R':
                horizontal += 1
            else:
                horizontal -= 1
        if (vertical == 0 and horizontal == 0):
            return True
        return False
s = Solution()
print s.judgeCircle("LDRRLRUULR")

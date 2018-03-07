#!/usr/bin/env python
# -*- conding:utf-8 -*-
__author__ = 'unicoe'
__date__ = '2017/8/27'
__time__ = '22:14'


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l1 = a.split('+')
        l2 = b.split('+')

        l3 = l1[1].split('i')
        l4 = l2[1].split('i')

        n1 = int(l1[0])
        n2 = int(l2[0])
        n3 = int(l3[0])
        n4 = int(l4[0])

        a1 = n1*n2
        a2 = n3*n4
        a3 = n1*n4 + n2*n3

        a2 = -a2
        a = a1+a2
        ans = str(a)+'+'+str(a3)+'i'
        return ans

s = Solution()
s.complexNumberMultiply("1+1i", "1+1i")

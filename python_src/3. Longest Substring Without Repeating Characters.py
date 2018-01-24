#!/usr/bin/env python
# -*- conding:utf-8 -*-
__author__ = 'unicoe'
__date__ = '2018/1/24'
__time__ = '20:41'


class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        #time O(len(str)*2)    TLE
        #space O(len(str)+26)
        """
        charSet = set()
        max = 0
        cur = 0

        for i in range(len(s)):
            cur = 0
            for j in range(i, len(s)):
                if s[j] not in charSet:
                    charSet.add(s[j])
                    cur += 1
                else:
                    charSet.clear()
                    charSet.add(s[j])
                    if cur > max:
                        max = cur
                    cur = 1

                if cur > max:
                    max = cur
            charSet.clear()

        if cur > max:
            return cur
        return max

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type ;s: str
        :rtype: int
        思想就是像字符串匹配的KMP，将位置记录下来
        当失配时，返回同当前字符串相同的字符的下一个
        """
        maxLen = start = 0
        charDict = {}

        for i in range(len(s)):
            if s[i] in charDict and start <= charDict[s[i]]:
                start = charDict[s[i]] + 1
            else:
                maxLen = max(maxLen, i - start + 1)
            charDict[s[i]] = i
        return maxLen





s = Solution()
print(s.lengthOfLongestSubstring("qwnfenpglqdq"))
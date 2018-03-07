import re
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        str1 = 'qwertyuiop'
        str2 = 'asdfghjkl'
        str3 = 'zxcvbnm'
        t1 = 0
        t2 = 0
        t3 = 0
        l = []
        for s in words:
            str = s.lower()
            for i in xrange(len(str)):
                if str1.find(str[i]) != -1 and t1 == 0:
                    t1 = 1
                if str2.find(str[i]) != -1 and t2 == 0:
                    t2 = 1
                if str3.find(str[i]) != -1 and t3 == 0:
                    t3 = 1

            if (t1+t2+t3) == 1:
                l.append(s)
            t1 = 0
            t2 = 0
            t3 = 0
        return l

s = Solution()
print s.findWords(["Hello", "Alaska", "Dad", "Peace"])

#understand the regex
def findWords(self, words):
    return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
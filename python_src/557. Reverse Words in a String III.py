class Solution(object):
    # def reverseWords(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     l = s.split(' ')
    #     ns = ''
    #     for w in l:
    #         le = len(w)-1
    #         while(le>=0):
    #             ns += w[le]
    #             le -= 1
    #         ns += ' '
    #     nns = ''
    #     for i in xrange(len(ns)-1):
    #         nns += ns[i]
    #     return nns

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([substr[::-1] for substr in s.split(' ')])

    def reverseWords1(self, s):
        """
        :type s: str
        :rtype: str
        """
        ws = s.split()
        l = []
        for w in ws:
            l.append(w[::-1])
        return ' '.join(l)

s = Solution()
print s.reverseWords("Let's take LeetCode contest")
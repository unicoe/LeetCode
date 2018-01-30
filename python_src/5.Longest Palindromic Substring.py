class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        chlStr = self.chandleStr(s)

        id = 0
        mxLen = 0

        ls = {}
        #print(chlStr)
        for i in range(1,len(chlStr)):
            ls[i] = 1
            if mxLen > i:
                ls[i] = min(ls[2*id-i], mxLen-i)

            while i-ls[i] >= 1 and i+ls[i] < len(chlStr) and chlStr[i+ls[i]] == chlStr[i-ls[i]]:
                ls[i] += 1
            if i + ls[i] > mxLen:
                mxLen = i + ls[i]
                id = i
        res = 0
        ii = 0
        for idx in ls:
            if ls[idx] > res:
                res = ls[idx]-1
                ii = idx

        #print(ii)
        ans = "".join(chlStr[ii-res:ii+res+1].split('#'))
        return ans


    def chandleStr(self,s):
        sl = []
        sl.append('$')
        for idx_s in s:
            sl.append('#')
            sl.append(idx_s)
        sl.append('#')

        return ''.join(sl)


s = Solution()
res = s.longestPalindrome("abccbad")
print(res)
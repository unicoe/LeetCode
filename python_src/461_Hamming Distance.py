class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        lx = []
        ly = []
        while(x != 0):
            lx.append(x % 2)
            x = x/2
        for i in range(len(lx), 32):
            lx.append(0)
        while(y != 0):
            ly.append(y % 2)
            y = y/2
        for i in range(len(ly), 32):
            ly.append(0)
        cnt = 0
        for i in range(32):
            if lx[i] != ly[i]:
               cnt += 1
        return cnt




s = Solution()
print s.hammingDistance(1,4)
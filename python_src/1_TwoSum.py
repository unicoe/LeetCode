class Solution(object):
    def twoSum(self, nums, target):
        lens = len(nums)
        flag = False
        for i in xrange(lens):
            if flag== True:
                break
            for j in xrange(i+1, lens):
                if nums[i]+nums[j] == target:
                    l = []
                    l.append(i)
                    l.append(j)
                    flag = True
                    break
        return l

s = Solution()
l = s.twoSum([2, 7, 11, 15], 9)
print l
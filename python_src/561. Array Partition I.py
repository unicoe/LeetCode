class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        for i in xrange(0, len(nums)/2):
            sum += nums[i*2]
        return sum
s = Solution()
print s.arrayPairSum([1,3,2,4])
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        so easy。。。
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        resSet = set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    resSet.add(i)
        return list(resSet)

s = Solution()
res = s.intersection([1,2,3,1],[1])
print(res)
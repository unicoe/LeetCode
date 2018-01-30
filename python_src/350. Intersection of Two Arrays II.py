class Solution(object):
    def intersect(self, nums1, nums2):
        """
        将两个列表中相同的元素标记了，之后不再使用，就可以保证选出两个列表中的公共元素
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp

        resL = []
        viD1 = {}
        viD2 = {}

        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if nums1[i] == nums2[j] and i not in viD1 and j not in viD2:
                    viD1[i] = 1
                    viD2[j] = 1
                    resL.append(nums1[i])
        return resL


s = Solution()
res = s.intersect([1,2],[1,1])
print(res)
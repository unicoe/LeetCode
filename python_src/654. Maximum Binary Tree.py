#!/usr/bin/env python
# -*- conding:utf-8 -*-
__author__ = 'unicoe'
__date__ = '2017/8/27'
__time__ = '21:40'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        maxl = 0

        lens = len(nums)
        tmp = nums[0]
        for i in xrange(lens):
            if tmp < nums[i]:
                maxl = i
                tmp = nums[i]

        l1 = []
        l2 = []
        for i in xrange(0,maxl,1):
            l1.append(nums[i])
        for i in xrange(maxl+1, lens, 1):
            l2.append(nums[i])

        node = TreeNode(tmp)
        node.left = self.constructMaximumBinaryTree(l1)
        node.right = self.constructMaximumBinaryTree(l2)

        return node

    def printTree(self, TreeNode):
        if TreeNode is not None:
            print TreeNode.val
        if TreeNode.left is not None:
            self.printTree(TreeNode.left)
        if TreeNode.right is not None:
            self.printTree(TreeNode.right)

s = Solution()
tree = s.constructMaximumBinaryTree( [3,2,1,6,0,5])
s.printTree(tree)



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        if t2 == None:
            return t1

        sumVal = 0
        flag = False
        if t1 != None:
            sumVal += t1.val
            flag = True
        if t2 != None:
            sumVal += t2.val
            flag = True
        if flag == False:
            ansT = None
        else:
            ansT = TreeNode(sumVal)

        if ansT != None:
            s = Solution()
            if t1 == None and t2 != None:
                ansL = s.mergeTrees(t1, t2.left)
                ansR = s.mergeTrees(t1, t2.right)
            elif t2 == None and t1 != None:
                ansL = s.mergeTrees(t1.left, t2)
                ansR = s.mergeTrees(t1.right, t2)
            else:
                ansL = s.mergeTrees(t1.left, t2.left)
                ansR = s.mergeTrees(t1.right, t2.right)

            ansT.left = ansL
            ansT.right = ansR

        return ansT

#reference key:
class Solution(object):
    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans

s = Solution()
f = None
print (s and f)
# None
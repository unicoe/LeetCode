class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Two things to make the code simple:
#
# Whenever one of the two ListNode is null, replace it with 0.
# Keep the while loop going when at least one of the three conditions is met.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        prev = ListNode(0)
        head = prev
        carry = 0
        while(l1 != None or l2 != None or carry != 0):
            cur = ListNode(0)
            sum = carry
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            if l1 != None:
                sum += l1.val
                l1 = l1.next

            cur.val = sum % 10
            carry = sum / 10
            prev.next = cur
            prev = cur

        return head.next

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         ans = ListNode(0)
#         tmp = ans
#         tmpsum = 0
#         while True:
#             if l1 != None:
#                 tmpsum += l1.val
#                 l1 = l1.next
#             if l2 != None:
#                 tmpsum += l2.val
#                 l2 = l2.next
#             tmp.val = tmpsum % 10
#             tmpsum //= 10
#             if l1 == None and l2 == None and tmpsum == 0:
#                 break
#             tmp.next = ListNode(0)
#             tmp = tmp.next
#         return ans

# create node method kengdie
def createList(l):
    nod = ListNode(None)
    tmp = nod
    for i in l:
        nod.val = i
        nod.next = None    # important
        nod = nod.next
    return tmp

def printL(l):
    print 'printL'
    while(l != None):
        print l.val
        l = l.next

ll1 = createList([0])
ll2 = createList([5])

s = Solution()

ans = s.addTwoNumbers(ll1, ll2)
printL(ans)


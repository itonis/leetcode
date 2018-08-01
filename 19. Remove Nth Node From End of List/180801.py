# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cNode = head
        for _ in range(n):
            cNode = cNode.next
        if not cNode:
            return head.next
        frontTail = head
        backHead = head.next.next
        while cNode.next:
            frontTail = frontTail.next
            backHead = backHead.next
            cNode = cNode.next
        frontTail.next = backHead
        return head
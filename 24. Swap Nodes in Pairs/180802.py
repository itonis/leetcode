
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        
        currPair = head
        head = currPair.next
        nextPair = currPair.next.next
        if not nextPair:
            head.next = currPair
            currPair.next = None
            return head
        while nextPair.next:
            (currPair.next).next = currPair
            currPair.next = nextPair.next
            currPair = nextPair
            nextPair = nextPair.next.next
            if not nextPair:
                break
        (currPair.next).next = currPair
        currPair.next = nextPair
        return head
    
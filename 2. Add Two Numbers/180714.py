# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ret = ListNode(0)
        nowNode = ret
        while nowNode:
            ss = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = ss // 10
            nowNode.val = ss % 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2 or carry:
                nowNode.next = ListNode(0)
            nowNode = nowNode.next
        return ret
        
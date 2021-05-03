# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = [(n.val, i) for i, n in enumerate(lists) if n]
        if not q:
            return None
        head = ListNode()
        tail = head
        heapq.heapify(q)
        while len(q) > 1:
            _, ci = heapq.heappop(q)
            current = lists[ci]
            second = q[0][0]
            tail.next = current
            while current.val <= second:
                tail = current
                if current.next:
                    current = current.next
                else:
                    current = None
                    break
            if current:
                heapq.heappush(q, (current.val, ci))
                lists[ci] = current
        tail.next = lists[q[0][1]]
        return head.next

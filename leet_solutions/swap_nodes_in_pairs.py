# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        front = ListNode(-1)
        front.next = head

        l = head
        r = head.next
        head = front

        while True:
            l.next = r.next
            front.next = r
            r.next = l
            front = l

            if l.next is None:
                break
            l = l.next

            if l.next is None:
                break
            r = l.next

        return head.next

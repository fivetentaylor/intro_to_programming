# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_list(iterable):
    head = ListNode(0)
    ptr = head
    for i in iterable:
        ptr.next = ListNode(i)
        ptr = ptr.next

    if head.next:
        return head.next


def linked_to_list(linked):
    ptr = linked
    l = []
    while ptr:
        l.append(ptr.val)
        ptr = ptr.next

    return l


def swap_pairs(head: ListNode) -> ListNode:
    # if empty or sinlge node list just return
    if head is None or head.next is None:
        return head

    # put a dummy node at the front of the list
    # so the first swap can be handled the same
    # as the subsequent swaps
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

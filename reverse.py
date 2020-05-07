import pudb

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(head):
    tmp = head
    vals = []
    while tmp:
        vals.append(str(tmp.val))
        tmp = tmp.next

    return '->'.join(vals)


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # Put dummy node at front so algorithm is same
    # for first swap as others
    tmp = ListNode(1000)
    tmp.next = head

    head = tmp
    front = head
    pivot = head

    while True:
        for i in range(k):
            if pivot.next is None:
                break
            pivot = pivot.next

        for j in range(i):
            print(print_list(head))
            swap = front.next
            front.next = swap.next
            swap.next = pivot.next
            pivot.next = swap

        print(print_list(head))

        for i in range(k):
            if front.next is None:
                break
            front = front.next

        print(front.val)

        if front.next is None:
            break

        pivot = front

        print()

    return head.next

head = ListNode(0)
tmp = head
for i in range(1, 10):
    tmp.next = ListNode(i)
    tmp = tmp.next

#pudb.set_trace()
head = reverseKGroup(head, 4)


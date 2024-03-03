class ListNode:
    def __init__(self, node, value):
        self.node = node
        self.value = value
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        a = b = c = ListNode(0, head)
        i = 0
        while c.next.next:
            i = i + 1
            if i >= n:
                b = b.next
            c = c.next
        b.next = b.next.next
        return a.next

from common import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        prev = dummy
        while head:
            if head.val != val:
                prev.next = head
                prev = prev.next
            head = head.next
        return dummy.next


if __name__ == "__main__":
    next = ListNode()
    next.val = 1
    head = None
    for v in [2, 2, 1]:
        head = ListNode()
        head.val = v
        head.next = next
        next = head

    res = Solution().removeElements(head, 2)
    pass

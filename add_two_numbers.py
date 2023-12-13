# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


def array_2_list(nums):
    tail = iter = ListNode()
    for n in nums:
        iter.next = ListNode(n)
        iter = iter.next
    return tail.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        tail = result = ListNode()
        tens = 0
        while first != None or second != None:
            v1 = 0 if first is None else first.val
            v2 = 0 if second is None else second.val
            new_result = ListNode()
            if v1 + v2 + tens > 9:
                new_result.val = v1 + v2 + tens - 10
                tens = 1
            else:
                new_result.val = v1 + v2 + tens
                tens = 0
            result.next = new_result
            result = result.next
            first = first.next if first is not None else None
            second = second.next if second is not None else None

        if tens > 0:
            result.next = ListNode(1)

        return tail.next


if __name__ == "__main__":
    l1 = array_2_list([9,9,9,9,9,9,9])
    l2 = array_2_list([9,9,9,9])
    print(Solution().addTwoNumbers(l1, l2))
    pass

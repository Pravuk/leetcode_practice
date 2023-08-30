# Definition for singly-linked list.
from typing import Optional

from common import ListNode, list_from_array


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        node = dummy_head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        else:
            node.next = list2

        return dummy_head.next


if __name__ == "__main__":
    s = Solution()
    l = s.mergeTwoLists(list_from_array([1, 3, 4]), list_from_array([1, 2, 5]))
    pass

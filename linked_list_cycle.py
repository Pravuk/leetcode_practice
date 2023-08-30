from typing import Optional

from common import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and slow.next and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_from_array(nums: List[int]) -> Optional[ListNode]:
    if len(nums) == 0:
        return None

    head = ListNode(nums[0])
    prev = head
    for n in nums[1:]:
        node = ListNode(n)
        prev.next = node
        prev = node

    return head


if __name__ == "__main__":
    l = list_from_array([1, 2, 3, 4, 5])

    pass

import time
from typing import List, Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        fast_counter = 0
        slow_counter = 0

        while fast and slow and fast.next:

            fast = fast.next.next
            fast_counter += 2
            slow = slow.next
            slow_counter += 1
            if fast_counter < slow_counter:
                break
        if slow == fast:
            return slow
        return None


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    head = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(1)
    node5 = ListNode(1)
    node6 = ListNode(1)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = None
    ret_val = sol_obj.hasCycle(head)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

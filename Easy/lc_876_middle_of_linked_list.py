import time
from typing import List, Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next

        return slow.val


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    head = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5, next=ListNode(6, None))))))

    ret_val = sol_obj.middleNode(head=head)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

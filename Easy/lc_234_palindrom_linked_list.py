import time
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val_list = list()
        while head.next:
            val_list.append(head.val)
            head = head.next
        val_list.append(head.val)
        i = 0
        val_len = len(val_list)
        while i <= val_len / 2:

            if val_list[i] != val_list[val_len - i - 1]:
                return False
            i += 1
        return True

    def reverse(self, head: Optional[ListNode]) -> ListNode:
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


if "__main__" == __name__:
    start_time = time.time()
    s = ListNode(1, ListNode(2, ListNode(3, ListNode(1, None))))
    s = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    sol_obj = Solution()
    # ret_val = sol_obj.isPalindrome(head=s)
    # print(ret_val)
    ret_val = sol_obj.reverse(head=s)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)
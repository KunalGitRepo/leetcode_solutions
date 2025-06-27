import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    l1 = ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=None)))
    l2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=5, next=None)))
    ret_val = sol_obj.mergeTwoLists(list1=l1, list2=l2)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

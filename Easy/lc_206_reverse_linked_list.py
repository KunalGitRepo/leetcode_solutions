from typing import Optional
import time


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = list()
        if not head:
            return head
        while head:
            node_list.append(head)
            head = head.next
        new_head = node_list[-1]
        new_l2 = new_head
        count = len(node_list) - 2
        while count >= 0:
            node_list[count].next = None
            new_head.next = node_list[count]
            new_head = new_head.next
            count -= 1

        return new_l2




if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    l1 = ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=None)))
    ret_val = sol_obj.reverseList(head=l1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)
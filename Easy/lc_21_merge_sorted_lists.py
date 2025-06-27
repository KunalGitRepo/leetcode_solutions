from typing import Optional
import time


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        ret_head = None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1 and list2:
            if list1.val < list2.val:
                new_head = list1
                ret_head = list1
                list1 = list1.next
            else:
                new_head = list2
                ret_head = list2
                list2 = list2.next
        else:
            if not list1:
                return list2
            if not list2:
                return list1

        while list1 and list2:
            if list1.val < list2.val:
                new_head.next = list1
                new_head = new_head.next
                list1 = list1.next
            else:
                new_head.next = list2
                new_head = new_head.next
                list2 = list2.next

        if not list1:
            new_head.next = list2
        if not list2:
            new_head.next = list1
        return ret_head

    def print_nodes(self, head):
        while head:
            print(head.val)
            head = head.next


if __name__ == "__main__":
    start_time = time.time()
    root1 = ListNode(-6, ListNode(-5, ListNode(1, ListNode(2, None))))
    root2 = ListNode(0, None)
    sol_obj = Solution()
    ret_val = sol_obj.mergeTwoLists(root1, root2)
    print(ret_val)
    sol_obj.print_nodes(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

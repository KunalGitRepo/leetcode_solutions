import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    #     prev_node = ListNode()
    #     new_head = head
    #     node = head
    #     while node:
    #         if node.val == val:
    #             if prev_node.val:
    #                 prev_node.next = node.next
    #                 if node.next:
    #                     node = node.next
    #                 else:
    #                     break
    #             else:
    #                 # prev_node = node
    #                 if node.next:
    #                     node = node.next
    #                 else:
    #                     node.val = ''
    #                     break
    #                 # prev_node.next = None
    #                 # prev_node.val = None
    #                 new_head = node
    #         else:
    #             prev_node = node
    #             if node.next:
    #                 node = node.next
    #             else:
    #                 break
    #
    #     return new_head

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        prev_node, curr_node = dummy, head

        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next

        return dummy.next


if __name__ == "__main__":
    start_time = time.time()
    n = 4
    k = 7
    sol_obj = Solution()
    # head = ListNode(val=4, next=ListNode(2, next=(ListNode(val=2, next=ListNode(3)))))
    # head = ListNode(val=1, next=ListNode(2, next=(ListNode(val=3, next=ListNode(1, next=ListNode(3, next=ListNode(1)))))))
    head = ListNode(val=7, next=ListNode(7, next=(ListNode(val=7, next=ListNode(7)))))
    # head = ListNode(val=5, next=ListNode(4, next=(ListNode(val=2, next=ListNode(1)))))
    # head = ListNode(val=1, next=ListNode(10000))
    ret_val = sol_obj.removeElements(head=head, val=k)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

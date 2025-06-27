import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        count1 = 0
        count2 = 0
        new_head_a = headA
        new_head_b = headB
        while new_head_a or new_head_b:
            if new_head_a:
                count1 += 1
                new_head_a = new_head_a.next
            if new_head_b:
                count2 += 1
                new_head_b = new_head_b.next

        if new_head_a != new_head_b:
            return None

        if count1 > count2:
            for i in range(count1 - count2):
                headA = headA.next
        else:
            for i in range(count2 - count1):
                headB = headB.next

        while headA:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return headA

    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # count1 = 0
        # count2 = 0
        # temp1 = headA
        # temp2 = headB
        #
        # while temp1 or temp2:
        #     if temp1:
        #         count1 = count1 + 1
        #         temp1 = temp1.next
        #     if temp2:
        #         count2 = count2 + 1
        #         temp2 = temp2.next
        #
        # count = count1 - count2
        #
        # if count < 0:
        #     while count != 0:
        #         headB = headB.next
        #         count = count + 1
        # else:
        #     while count != 0:
        #         headA = headA.next
        #         count = count - 1
        # while headA:
        #     if headA == headB:
        #         return headA
        #     headA = headA.next
        #     headB = headB.next
        # return headA


if __name__ == "__main__":
    start_time = time.time()
    n = 4
    k = 7
    sol_obj = Solution()
    # head = ListNode(val=4, next=ListNode(2, next=(ListNode(val=2, next=ListNode(3)))))
    head1 = ListNode(4, next=ListNode(1, next=ListNode(8, next=ListNode(4, next=ListNode(5)))))
    head2 = ListNode(5, next=ListNode(6, next=ListNode(1, next=ListNode(8, ListNode(4, next=ListNode(5))))))
    ret_val = sol_obj.getIntersectionNode(headA=head1, headB=head2)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

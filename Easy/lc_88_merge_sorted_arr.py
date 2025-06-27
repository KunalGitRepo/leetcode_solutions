import time
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        curr_pointer = 0
        zeros_size = n
        for num in nums2:
            while curr_pointer < len(nums1):
                if nums1[curr_pointer] > num:
                    nums1.pop(-1)
                    nums1.insert(curr_pointer, num)
                    curr_pointer += 1
                    zeros_size -= 1
                    break
                elif nums1[curr_pointer] == 0 and curr_pointer >= len(nums1) - zeros_size:
                    nums1.pop(-1)
                    nums1.insert(curr_pointer, num)
                    curr_pointer += 1
                    zeros_size -= 1
                    break
                curr_pointer += 1

        # if zeros_size > 0:
        #     a = nums1[:-zeros_size]
        #     b = nums2[-zeros_size:]
        #     nums1 = a + b
        print(nums1)


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    l1 = [1, 2, 3, 0, 0, 0]
    l2 = [2, 5, 6]
    # l1 = [1]
    # l2 = []
    l1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    l2 = [1, 2, 2]
    ret_val = sol_obj.merge(nums1=l1, m=3, nums2=l2, n=3)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

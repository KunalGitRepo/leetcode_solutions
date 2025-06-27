import time
from typing import List, Optional


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out_list = list()
        for n in nums1:
            if n in nums2:
                num_ind = nums2.index(n)
                in_num = -1
                for i in nums2[num_ind:]:
                    if i > n:
                        in_num = i
                        break
                out_list.append(in_num)
        return out_list


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    a = [4, 1, 2]
    b = [1, 3, 4, 2]
    a = [2, 4]
    b = [1, 2, 3, 4]
    ret_val = sol_obj.nextGreaterElement(nums1=a, nums2=b)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

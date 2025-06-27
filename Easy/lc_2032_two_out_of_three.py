import time
from typing import List, Optional


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        n1_n2_set = list(set(nums1) & set(nums2))
        n1_n3_set = list(set(nums1) & set(nums3))
        n2_n3_set = list(set(nums2) & set(nums3))
        out_list = list(set(n1_n2_set + n2_n3_set + n1_n3_set))
        return out_list


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    n1 = [1, 1, 3, 2]
    n2 = [2, 3]
    n3 = [3]
    # n1 = [3, 1]
    # n2 = [2, 3]
    # n3 = [1, 2]
    # n1 = [1, 2, 2]
    # n2 = [4, 3, 3]
    # n3 = [5]
    ret_val = sol_obj.twoOutOfThree(nums1=n1, nums2=n2, nums3=n3)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

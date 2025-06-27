import time
from typing import List, Optional


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_sum = -1
        new_max_sum = -1
        for outer_ind, outer_num in enumerate(nums):
            out_list = list(str(outer_num))
            out_list.sort()
            for inner_ind, inner_num in enumerate(nums[outer_ind+1:]):
                in_list = list(str(inner_num))
                in_list.sort()
                if out_list[-1] == in_list[-1]:
                    new_max_sum = outer_num + inner_num

                # if new_max_sum > max_sum:
                #     print("NUM1 %s and NUM2 %s = SUM %s" % (outer_num, inner_num, new_max_sum))
                max_sum = max(new_max_sum, max_sum)

        return max_sum


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    # num = [51, 71, 17, 24, 42, 88, 88]
    num = [1, 2, 3, 4]
    # num = [31, 25, 72, 79, 74]
    # num = [52, 32, 24, 6, 3, 89, 100, 3, 5, 3]
    # num = [19, 12, 52, 8, 3, 58]
    # num = [51, 1, 98, 73, 84, 11, 100, 100, 75]
    # num = [1573, 2030, 885, 1987, 2097, 1709, 1524, 1335, 1361, 1344, 261, 484, 1025, 2347, 2124, 515, 1404, 1849, 1148]
    # num = [1573, 1987, 2097, 2347, 2124]
    # num = [68, 8, 100, 84, 80, 14, 88]
    # num = [5, 53, 35, 88, 77, 1, 66, 57]
    ret_val = sol_obj.maxSum(nums=num)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

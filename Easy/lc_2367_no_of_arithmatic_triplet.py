import time
from typing import List, Optional
import math


class Solution:

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        out_list = list()
        count = 0
        num_len = len(nums) - 1
        for ind, val in enumerate(nums):
            d = val + diff
            if d in nums[ind:]:
                out_list.append(ind)
                if ind < num_len - 1:
                    in_ind = nums.index(d, ind, num_len+1)
                    out_list.append(in_ind)
                    if d + diff in nums[in_ind:]:
                        count += 1
                        out_list = list()

        return count


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    n = [0,1,4,6,7,10]


    ret_val = sol_obj.arithmeticTriplets(nums=n, diff=3)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

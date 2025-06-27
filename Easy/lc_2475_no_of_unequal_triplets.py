import time
from typing import List, Optional
import math


class Solution:

    def unequalTriplets(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0

        if len(nums) == 3 and len(set(nums)) == 3:
            return 1

        count = 0
        for ind, val in enumerate(nums):
            for in_ind, in_val in enumerate(nums[ind+1:]):
                for k in nums[ind+in_ind+2:]:
                    if val != in_val and in_val != k and val != k:
                        count += 1
        return count


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    n = [4, 4, 2, 4, 3]
    n = [1, 1, 1, 1, 1, 1, 3, 4]

    ret_val = sol_obj.unequalTriplets(nums=n)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

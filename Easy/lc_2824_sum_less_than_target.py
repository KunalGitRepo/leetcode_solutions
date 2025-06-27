import time
from typing import List, Optional


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for out_ind, out_num in enumerate(nums):
            for in_num in nums[out_ind + 1:]:
                if out_num + in_num < target:
                    count += 1
        return count


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    num = [-1, 1, 2, 3, 1]
    num = [-6, 2, 5, -2, -7, -1, 3]
    ret_val = sol_obj.countPairs(nums=num, target=-2)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

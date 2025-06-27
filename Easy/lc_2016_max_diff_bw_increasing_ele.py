import time
from typing import List, Optional


class Solution:

    def maximumDifference_orig(self, nums: List[int]) -> int:
        max_diff = -1
        for out_ind, out_val in enumerate(nums):
            temp_diff = -1
            for in_val in nums[out_ind:]:
                d = in_val - out_val
                if in_val > out_val and d > temp_diff:
                    temp_diff = d
            max_diff = max(max_diff, temp_diff)
        return max_diff

    def maximumDifference(self, nums: List[int]) -> int:
        minn = 1e9
        diff = -1
        for i in nums:
            if i <= minn:
                minn = i
            else:
                diff = max(diff, i - minn)
        return diff



if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    # a = [17,18,5,4,6,1]
    # a = [5,4,3,2,1]
    a = [7,1,5,4, 10]

    ret_val = sol_obj.maximumDifference(nums=a)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

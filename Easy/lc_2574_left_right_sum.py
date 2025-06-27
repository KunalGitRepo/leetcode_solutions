import time
from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        count = 0
        out_list = list()
        while count < len(nums):
            out_list.append(abs(sum(nums[:count]) - sum(nums[count+1:])))
            count += 1
        return out_list


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    l1 = [10, 4, 8, 3]
    l1 = [1]
    ret_val = sol_obj.leftRigthDifference(nums=l1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

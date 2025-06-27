import time
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x * x, nums)))


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    l1 = [1, 2, 3, 0, 0, 0]
    l2 = [2, 5, 6]
    # l1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    # l2 = [1, 2, 2]
    ret_val = sol_obj.sortedSquares(nums=l1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

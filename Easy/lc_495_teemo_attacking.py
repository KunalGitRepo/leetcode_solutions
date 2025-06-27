import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_poison = duration
        for ind, val in enumerate(timeSeries[1:]):
            diff = val - timeSeries[ind]
            total_poison = total_poison + min(diff, duration)
            # if diff < duration:
            #     total_poison = total_poison + diff
            # else:
            #     total_poison = total_poison + duration
        return total_poison


if "__main__" == __name__:
    start_time = time.time()
    l = [1, 2]
    b = 2
    sol_obj = Solution()
    ret_val = sol_obj.findPoisonedDuration(timeSeries=l, duration=b)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

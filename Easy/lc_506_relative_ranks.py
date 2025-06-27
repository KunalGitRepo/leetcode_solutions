import time
from typing import List, Optional
import math


class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        out_arr = [i for i in score]
        count = 1
        for j in sorted(score, reverse=True):
            max_ind = out_arr.index(j)
            if count == 1:
                out_arr[max_ind] = "Gold Medal"
            elif count == 2:
                out_arr[max_ind] = "Silver Medal"
            elif count == 3:
                out_arr[max_ind] = "Bronze Medal"
            else:
                out_arr[max_ind] = str(count)
            count += 1

        out_arr = [str(i) for i in out_arr]
        return out_arr


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    n = [20, 100, 4, 6, 7, 10]

    ret_val = sol_obj.findRelativeRanks(score=n)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

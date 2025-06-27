import time
from typing import List, Optional
import math


class Solution:

    def totalNumbers(self, digits: List[int]) -> int:

        for ind, val in enumerate(digits):
            for in_ind, in_val in enumerate(digits[ind+1:]):
                for k in digits[ind+in_ind+2:]:
                    print(val, in_val, k)
        return 0


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    w1 = [1, 2, 3, 4]
    ret_val = sol_obj.totalNumbers(digits=w1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

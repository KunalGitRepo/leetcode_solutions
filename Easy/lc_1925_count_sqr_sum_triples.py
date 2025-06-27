import time
from typing import List, Optional
import math


class Solution:

    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(3, n):
            for j in range(i, n):
                num = math.sqrt(i * i + j * j)
                if float(num).is_integer() and num <= n:
                    count += 2
                    st = "{0}, {1} and {1}, {0}".format(i, j)
                    print(st)
        return count



if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    a = 10

    ret_val = sol_obj.countTriples(n=a)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

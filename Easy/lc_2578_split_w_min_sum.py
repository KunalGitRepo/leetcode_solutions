import time
from typing import List, Optional


class Solution:

    def splitNum(self, num: int) -> int:
        num_str_list = list(str(num))
        num_str_list.sort()
        num1 = str()
        num2 = str()
        count = 1
        for i in num_str_list:
            if count % 2 == 1:
                num1 += i
            else:
                num2 += i
            count += 1
        out = int(num1) + int(num2)
        return out


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    r = 678
    r = 4325
    r = 1234
    ret_val = sol_obj.splitNum(num=r)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

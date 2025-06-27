import time
from typing import List, Optional


class Solution:
    def __init__(self):
        pass

    def digitCount(self, num: str) -> bool:
        count = 0
        for val in num:
            if num.count(str(count)) != int(val):
                return False
            count += 1
        return True


if "__main__" == __name__:
    start_time = time.time()
    num = "1210"
    num = "030"
    sol_obj = Solution()
    ret_val = sol_obj.digitCount(num=num)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

import time
from typing import List, Optional


class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = str()
        if -6 <= num <= 6:
            return str(num)
        rem = abs(num) // 7
        mod = abs(num) % 7
        if rem <= 6:
            ans = str(rem) + str(mod)
            return ans if num >= 0 else '-' + ans
        while True:
            if rem <= 6:
                ans = str(rem) + str(mod) + ans
                break
            else:
                ans = str(mod) + ans
            mod = rem % 7
            rem = rem // 7
        return ans if num >= 0 else '-' + ans


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    n1 = -1
    ret_val = sol_obj.convertToBase7(num=n1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

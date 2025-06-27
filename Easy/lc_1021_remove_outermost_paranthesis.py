import time
from typing import List, Optional
import math


class Solution:

    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        out = str()
        sub_str = str()
        for p in s:
            if p == '(':
                sub_str += p
                count += 1
            else:
                sub_str += p
                count -= 1

            if count == 0:
                out += sub_str[1:-1]
                sub_str = str()
            elif count <= -1:
                out += sub_str
                sub_str = str()
                count = 0

        if sub_str:
            out += sub_str
        return out


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    s1 = "(()())(())(()(()))"
    # s1 = ")()()()(())"
    ret_val = sol_obj.removeOuterParentheses(s=s1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

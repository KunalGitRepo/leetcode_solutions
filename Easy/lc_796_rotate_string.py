import time
from typing import List, Optional
import math


class Solution:

    # def rotateString(self, s: str, goal: str) -> bool:
    #     count = 0
    #     max = len(s)
    #     a = list(s)
    #     while count < max:
    #         letter = a.pop(0)
    #         a.append(letter)
    #         if ''.join(a) == goal:
    #             return True
    #         count += 1
    #     return False

    def rotateString(self, s: str, goal: str) -> bool:
        count = 0
        max = len(s)
        # if s == goal:
        #     return True
        while count < max:
            letters = s[0:count]
            rem_letter = s[count:]
            new_s = rem_letter + letters
            if new_s == goal:
                return True
            count += 1
        return False


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    s1 = "abcde"
    g = "cdeab"
    g = "abcde"
    ret_val = sol_obj.rotateString(s=s1, goal=g)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

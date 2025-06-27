import time
from typing import List, Optional
import math


class Solution:

    # def reverseOnlyLetters(self, s: str) -> str:
    #     fwd_counter = 0
    #     rev_counter = len(s) - 1
    #     out_str = ["" for _ in s]
    #     for i in s:
    #         if not i.isalpha():
    #             out_str[fwd_counter] = i
    #         fwd_counter += 1
    #     fwd_counter = 0
    #     for i in reversed(s):
    #         if i.isalpha():
    #             while out_str[fwd_counter] != "":
    #                 fwd_counter += 1
    #
    #             out_str[fwd_counter] = i
    #             fwd_counter += 1
    #
    #     return ''.join(out_str)

    def reverseOnlyLetters(self, s: str) -> str:
        only_str = str()
        for i in reversed(s):
            if i.isalpha():
                only_str += i

        # only_str = reversed(only_str)
        out_str = str()
        count = 0
        for i in s:
            if not i.isalpha():
                out_str += only_str[:count] + i
                only_str = only_str[count:]
            count += 1
        return out_str

    # def reverseOnlyLetters(self, s: str) -> str:
    #     fast_pointer = 0
    #     slow_pointer = 0
    #     out_arr = ['' for _ in s]
    #     for i in s:
    #         if i.isalpha():
    #             fast_pointer += 1
    #         else:
    #             sub_str = reversed(s[slow_pointer:fast_pointer])
    #             fast_pointer = slow_pointer = fast_pointer + 1
    #
    #
    #     return ''.join(out_str)


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    s1 = "Test1ng-Leet=code-Q!"
    s1 = "z<*zj"
    j = "j<*zz"
    ret_val = sol_obj.reverseOnlyLetters(s=s1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

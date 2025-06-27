import time
from typing import List


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_list = list()
        t_list = list()

        count = len(s) if len(s) > len(t) else len(t)

        for i in range(count):
            if i < len(s):
                if s[i] == '#' and s_list:
                    s_list.pop(-1)
                elif s[i] != '#':
                    s_list.append(s[i])

            if i < len(t):
                if t[i] == '#' and t_list:
                    t_list.pop(-1)
                elif t[i] != '#':
                    t_list.append(t[i])

        return s_list == t_list


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    n = 'a##c'
    n1 = '#a#c'
    # n = 'xywrrmp'
    # n1 = 'xywrrmu#p'
    # n = 'bxj##tw'
    # n1 = 'bxo#j##tw'
    n = 'y#fo##f'
    n1 = 'y#f#o##f'
    ret_val = sol_obj.backspaceCompare(s=n, t=n1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

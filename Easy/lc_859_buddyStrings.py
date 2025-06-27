import time
from typing import List


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diff_list = list()
        if len(s) != len(goal):
            return False

        if s == goal:
            if len(s) - len(set(s)) >= 1:
                return True
            else:
                return False

        if len(s) >= 2:
            if len(set(s)) == 1 and len(set(goal)) == 1:
                return True

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_list.append([s[i], goal[i]])

            if len(diff_list) > 2:
                return False

        if len(diff_list) != 2:
            return False

        if diff_list[0][0] != diff_list[1][1] or diff_list[0][1] != diff_list[1][0]:
            return False

        return True


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    n = 'acbd'
    n1 = 'abcd'
    # n = 'aa'
    # n1 = 'aa'
    # n = 'aaaaaaabc'
    # n1 = 'aaaaaaacb'
    # n = 'abab'
    # n1 = 'abab'
    ret_val = sol_obj.buddyStrings(s=n, goal=n1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)



# start_count = 0
#         end_count = len(s)
#         for i in range(end_count):
#             for j in range(start_count + 1, end_count):
#                 a = s[:i]
#                 b = s[j]
#                 c = s[i+1:j]
#                 d = s[i]
#                 e = s[j+1:]
#                 new_s = a + b + c + d + e
#                 if goal == new_s:
#                     return True
#             start_count += 1
#         return False
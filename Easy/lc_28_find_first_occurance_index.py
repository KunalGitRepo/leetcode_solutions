import time
from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match_pos = 0
        start_counter = haystack.find(needle[0])
        n_len = len(needle)
        cur_char = needle[0]
        counter = 0
        start_str = haystack[start_counter:]

        for a_char in start_str:
            if a_char == cur_char:
                start_counter += 1
                if start_counter == n_len:
                    return match_pos
                else:
                    cur_char = needle[start_counter]
            else:
                match_pos = counter + 1
                start_counter += 1
                cur_char = needle[start_counter]
            counter += 1
        return -1


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    s = "leetcode exercises sound delightful"
    s1 = "leeto"
    s = "sadbutsad"
    s1 = "sad"
    s = "mississippi"
    s1 = "issip"
    ret_val = sol_obj.strStr(haystack=s, needle=s1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

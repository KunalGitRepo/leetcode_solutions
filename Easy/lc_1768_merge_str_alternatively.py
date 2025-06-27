import time
from typing import List, Optional


class Solution:
    def __init__(self):
        pass

    def mergeAlternately(self, word1: str, word2: str) -> str:
        count = 0
        new_str = str()
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1

        while count < len(word1):
            if count < len(word2):
                new_str = new_str + word1[count] + word2[count]
                count += 1
            else:
                new_str = new_str + word1[count:]
                count = len(word1)
        if count < len(word2):
            new_str = new_str + word2[count:]
        return new_str


if "__main__" == __name__:
    start_time = time.time()
    list1 = "abcdefg"
    list2 = "abcdef"
    sol_obj = Solution()
    ret_val = sol_obj.mergeAlternately(word1=list1, word2=list2)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

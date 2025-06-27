import time
from typing import List


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s_list = sentence.split(" ")
        size = len(s_list) - 1
        if size == 0:
            if sentence[0] != sentence[-1]:
                return False
        if s_list[0][0] != s_list[-1][-1]:
            return False

        counter = 0

        while counter < size:
            if s_list[counter][-1] != s_list[counter+1][0]:
                return False
            counter += 1

        return True


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    s = "leetcode exercises sound delightful"
    s = "eetcode"
    # s = "Leetcode is cool"
    ret_val = sol_obj.isCircularSentence(sentence=s)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

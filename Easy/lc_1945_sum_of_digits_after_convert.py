import time
from typing import List


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_dict = dict()
        count = 1
        for n in range(97, 123):
            num_dict[chr(n)] = str(count)
            count += 1

        out = str()
        for st in s:
            out += num_dict[st]

        for kn in range(1, k+1):
            num_list = [int(i) for i in out]
            num_sum = sum(num_list)
            out = str(num_sum)
        return int(out)


if "__main__" == __name__:
    start_time = time.time()
    s1 = "iiii"
    k1 = 1
    s1 = "leetcode"
    k1 = 2
    sol_obj = Solution()
    ret_val = sol_obj.getLucky(s=s1, k=k1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

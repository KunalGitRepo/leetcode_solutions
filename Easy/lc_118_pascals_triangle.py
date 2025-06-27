import time
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        num = 1
        out_list = [[1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return out_list

        while num < numRows:
            num_sum = 0
            new_list = list()
            for i in out_list[-1]:
                num_sum += i
                new_list.append(num_sum)
                num_sum = i
            new_list.append(1)
            out_list.append(new_list)
            num += 1
        return out_list


if "__main__" == __name__:
    start_time = time.time()
    n = 6
    sol_obj = Solution()
    ret_val = sol_obj.generate(n)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

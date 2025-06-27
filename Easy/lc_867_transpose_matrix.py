import time
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        out_list = list()
        for out_ind, out_val in enumerate(matrix):
            for in_ind, in_val in enumerate(out_val):
                if len(out_list) < len(matrix[out_ind]):
                    out_list.append([])
                if out_ind <= len(out_list[in_ind]):
                    out_list[in_ind].append(in_val)
                # out_list[in_ind][out_ind] = in_val
        return out_list


if "__main__" == __name__:
    start_time = time.time()
    l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    l1 = [[1, 2, 3], [4, 5, 6]]
    sol_obj = Solution()
    ret_val = sol_obj.transpose(matrix=l1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

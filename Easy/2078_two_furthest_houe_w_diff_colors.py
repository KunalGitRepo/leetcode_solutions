import time
from typing import List, Optional


class Solution:

    def maxDistance(self, colors: List[int]) -> int:
        num_set = list(set(colors))
        num_dict = dict()
        for n in num_set:
            start_key = 'start_' + str(n)
            end_key = 'end_' + str(n)
            num_dict[start_key] = colors.index(n)

            for i in range(len(colors) - 1, -1, -1):
                if colors[i] == n:
                    num_dict[end_key] = i
                    break

        final_dist = 0
        for out_ind, out_val in enumerate(num_set):
            for in_val in num_set[out_ind+1:]:
                num_1_key_start = 'start_' + str(out_val)
                num_1_key_end = 'end_' + str(out_val)
                num_2_key_start = 'start_' + str(in_val)
                num_2_key_end = 'end_' + str(in_val)

                d1 = abs(num_dict[num_1_key_start] - num_dict[num_2_key_end])
                d2 = abs(num_dict[num_1_key_end] - num_dict[num_2_key_start])
                dist = max(d1, d2)
                if dist > final_dist:
                    final_dist = dist
        return final_dist


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    c = [1, 8, 3, 8, 3]
    # c = [1, 1, 1, 6, 1, 1, 1]
    # c = [6, 6, 6, 6, 6, 6, 6, 6, 6, 19, 19, 6, 6]
    # c = [0, 18, 10]

    ret_val = sol_obj.maxDistance(colors=c)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

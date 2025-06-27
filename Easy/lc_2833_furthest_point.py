import time
from typing import List, Optional


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_count = moves.count('L')
        r_count = moves.count('R')
        u_count = moves.count('_')
        if l_count > r_count:
            out_count = l_count + u_count - r_count
        else:
            out_count = r_count + u_count - l_count
        return out_count


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    move = "L_RL__R"
    # move = "_R__LL_"
    # move = "_______"
    ret_val = sol_obj.furthestDistanceFromOrigin(moves=move)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

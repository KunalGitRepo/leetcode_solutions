import time
from typing import List, Optional


class Solution:

    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_len = len(arr) - 1
        count = 0
        cur_max = -1
        while count <= arr_len:
            if arr[arr_len] > cur_max:
                new_max = arr[arr_len]
                arr[arr_len] = cur_max
                cur_max = new_max
            else:
                arr[arr_len] = -1
            arr_len -= 1
        return arr


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    # a = [17,18,5,4,6,1]
    a = [5,4,3,2,1]

    ret_val = sol_obj.replaceElements(arr=a)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

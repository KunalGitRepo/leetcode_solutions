import time
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        loop_len = len(arr)
        count = 0
        while count < loop_len:
            if arr[count] == 0:
                arr.insert(count, 0)
                arr.pop()
                count += 1
            count += 1
        return arr


if "__main__" == __name__:
    start_time = time.time()
    a = [1, 0, 2, 3, 0, 4, 5, 0]
    sol_obj = Solution()
    ret_val = sol_obj.duplicateZeros(arr=a)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

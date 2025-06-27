import time
from typing import List, Optional


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0 :
            return "0"
        hex_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                   10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        print(hex_map)
        res = str()
        if num < 0:
            num = num + 2 ** 32
        print(num)
        while num:
            res = hex_map[num % 16] + res
            num //= 16
        return res


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    n = 26
    n = -1
    ret_val = sol_obj.toHex(num=n)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

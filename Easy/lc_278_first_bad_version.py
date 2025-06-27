import time
from typing import List


class Solution:
    def __init__(self, bad):
        self.bad = bad

    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        # mid = int((l + r) / 2)
        # mid = l + (r - l) // 2
        while l <= r:
            mid = int((l + r) / 2)
            # if mid == 1:
            #     return mid
            # mid = l + (r - l) // 2
            if self.isBadVersion(version=mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

    def isBadVersion(self, version: int) -> bool:
        if version >= self.bad:
            return True
        else:
            return False


if "__main__" == __name__:
    start_time = time.time()
    l = 3
    bad = 2
    sol_obj = Solution(bad=bad)
    ret_val = sol_obj.firstBadVersion(n=l)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

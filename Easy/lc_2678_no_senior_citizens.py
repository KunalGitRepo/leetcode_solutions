import time
from typing import List, Optional


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = int()
        for data in details:
            age = int(data[11] + data[12])
            count = count + 1 if age > 60 else count
        return count


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    d = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
    ret_val = sol_obj.countSeniors(details=d)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

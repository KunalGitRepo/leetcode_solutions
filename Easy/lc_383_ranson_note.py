import time
from typing import List, Optional


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ret_val = True
        for s in ransomNote:
            if s in magazine:
                magazine = magazine.replace(s, '1', 1)
            else:
                ret_val = False
                break
        return ret_val


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    a = 'abaah'
    m = 'aabbaa'
    ret_val = sol_obj.canConstruct(ransomNote=a, magazine=m)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

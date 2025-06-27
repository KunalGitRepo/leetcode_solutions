import time
from typing import List, Optional


class Solution:
    def __init__(self):
        pass

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out_list = list()
        for i in range(left, right+1):
            flag = True
            num_list = list(str(i))
            if '0' in num_list:
                continue
            for j in num_list:
                if i % int(j) != 0:
                    flag = False
                    break

            if flag:
                out_list.append(i)
            # for j in str(i):
            #     if j == '0':
            #         flag = False
            #         break
            #     if i % int(j) != 0:
            #         flag = False
            #         break
            # if flag:
            #     out_list.append(i)
        return out_list


if "__main__" == __name__:
    start_time = time.time()
    num1 = 1
    num2 = 22
    sol_obj = Solution()
    ret_val = sol_obj.selfDividingNumbers(left=num1, right=num2)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

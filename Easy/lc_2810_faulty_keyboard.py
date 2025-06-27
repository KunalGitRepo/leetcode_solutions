import time
from typing import List, Optional


class Solution:
    # def finalString(self, s: str) -> str:
    #     out_str = str()
    #     for letter in s:
    #         if letter == 'i':
    #             out_list = list(out_str)
    #             out_list = reversed(out_list)
    #             out_str = ''.join(out_list)
    #         else:
    #             out_str += letter
    #     return out_str

    def finalString(self, s: str) -> str:
        i_count = s.count('i')
        flag = False if i_count % 2 == 0 else True
        tmp_str = str()
        out_str = str()
        for letter in s:
            if letter == 'i':
                # if i_count == 1 and flag:
                if i_count == 1:
                    # tmp_list = list(tmp_str)
                    # tmp_list = reversed(tmp_list)
                    # tmp_str = ''.join(tmp_list)
                    tmp_str = tmp_str[::-1]
                    out_str = tmp_str
                    tmp_str = str()
                else:
                    i_count -= 1
            else:
                tmp_str += letter
        out_str += tmp_str
        return out_str


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    st = "string"
    # st = 'strngii'
    st = 'poiinter'
    # st = 'viwif'
    ret_val = sol_obj.finalString(s=st)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

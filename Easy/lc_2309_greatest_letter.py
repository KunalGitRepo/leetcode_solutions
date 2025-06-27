import time
import string
from typing import List, Optional


class Solution:
    def greatestLetter(self, s: str) -> str:
        char_dict = dict()
        order = 1
        for i in string.ascii_lowercase:
            char_dict[i] = dict()
            char_dict[i]['count'] = 0
            char_dict[i]['lower'] = False
            char_dict[i]['upper'] = False
            char_dict[i]['order'] = order
            order += 1
        out_str = str()
        out_order = 0
        for c in s:
            char_dict[c.lower()]['count'] += 1
            if c.islower():
                char_dict[c.lower()]['lower'] = True
            else:
                char_dict[c.lower()]['upper'] = True
            j = c
            if char_dict[j.lower()]['count'] > 1:
                if char_dict[j.lower()]['lower'] and char_dict[j.lower()]['upper']:
                    if char_dict[j.lower()]['order'] > out_order:
                        out_str = j.upper()
                        out_order = char_dict[j.lower()]['order']

        # for j in char_dict.keys():
            # if char_dict[j.lower()]['count'] > 1:
            #     if char_dict[j.lower()]['lower'] and char_dict[j.lower()]['upper']:
            #         if char_dict[j.lower()]['order'] > out_order:
            #             out_str = j.upper()
            #             out_order = char_dict[j.lower()]['order']
        return out_str


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    st = "arRAzFif"
    ret_val = sol_obj.greatestLetter(s=st)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

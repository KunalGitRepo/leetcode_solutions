import time
from typing import List, Optional


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # keyboard = dict()
        # out_list = list()
        # keyboard[1] = "qwertyuiop"
        # keyboard[2] = "asdfghjkl"
        # keyboard[3] = "zxcvbnm"
        # for word in words:
        #     # count = 1
        #     flag = True
        #     letter = word[0]
        #     for count in range(1, len(keyboard.keys()) + 1):
        #         if letter.lower() in keyboard[count]:
        #             break
        #     for letter in word:
        #         if letter.lower() not in keyboard[count]:
        #             flag = False
        #             break
        #     if flag:
        #         out_list.append(word)
        # return out_list

        l1 = "qwertyuiop"
        l2 = "asdfghjkl"
        l3 = "zxcvbnm"
        res = []
        for word in words:
            w = word.lower()
            if len(set(l1 + w)) == len(l1) or len(set(l2 + w)) == len(l2) or len(set(l3 + w)) == len(l3):
                res.append(word)
        return res


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    w = ["Hello", "Alaska", "Dad", "Peace"]
    # w = ["a", "b"]
    ret_val = sol_obj.findWords(words=w)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

import time
from typing import List, Optional
import math


class Solution:

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        f = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        letter_dict = dict()
        count = 0
        for i in range(ord('a'), ord('z') + 1):
            letter_dict[chr(i)] = f[count]
            count += 1

        out = set()
        for word in words:
            morse_code = str()
            for w in word:
                morse_code += letter_dict[w]
            out.add(morse_code)
        return len(out)


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    w1 = ["gin","zen","gig","msg"]
    ret_val = sol_obj.uniqueMorseRepresentations(words=w1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

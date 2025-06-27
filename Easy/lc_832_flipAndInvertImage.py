import time
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        count = 0
        for line in image:
            out_image = list()
            # out_image.append(list())
            for pixel in line[::-1]:
                # out_image[count].append(1) if pixel == 0 else out_image[count].append(0)
                out_image.append(1) if pixel == 0 else out_image.append(0)
            image[count] = out_image
            count += 1
        return image


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    n = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    n = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    ret_val = sol_obj.flipAndInvertImage(image=n)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

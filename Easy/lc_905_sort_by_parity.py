import time
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        count = 0
        odd_count = 0
        while count <= nums_len:
            if nums[count] % 2 == 1:
                num = nums[count]
                nums.pop(count)
                nums.append(num)
                count -= 1
                odd_count += 1
            count += 1
            if odd_count + count == nums_len:
                break
        return nums


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    n = [1, 2, 3, 4]
    n = [1, 3, 1, 1, 1]
    ret_val = sol_obj.sortArrayByParity(nums=n)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

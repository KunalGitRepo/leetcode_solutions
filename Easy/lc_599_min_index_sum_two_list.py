import time
from typing import List, Optional


class Solution:
    def __init__(self):
        pass

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) > len(list2):
            list2, list1 = list1, list2

        val_list = []
        length = 9999
        for index, val in enumerate(list1):
            if val in list2:
                inner_index = list2.index(val)
                new_len = index + inner_index
                if length == new_len:
                    val_list.append(val)
                    length = new_len
                elif length > new_len:
                    val_list = list()
                    val_list.append(val)
                    length = new_len
        return val_list


if "__main__" == __name__:
    start_time = time.time()
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "Burger King", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    list1 = ["happy", "sad", "good"]
    list2 = ["sad", "happy", "good"]
    list1 = ["happy", "sad", "good"]
    list2 = []
    sol_obj = Solution()
    ret_val = sol_obj.findRestaurant(list1=list1, list2=list2)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

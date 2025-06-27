import time
import string
from typing import List, Optional



class MyQueue:

    def __init__(self):
        self.queue = list()

    def push(self, x: int) -> None:
        return self.queue.append(x)

    def pop(self) -> int:
        tmp_list = list()
        while len(self.queue) > 1:
            tmp_list.insert(0, self.queue.pop())
        ret_num = self.queue.pop()
        self.queue = tmp_list[:]
        return ret_num

    def peek(self) -> int:
        tmp_list = self.queue[:]
        while len(self.queue) > 1:
            self.queue.pop()
        ret_num = self.queue.pop()
        self.queue = tmp_list[:]
        return ret_num

    def empty(self) -> bool:
        return False if self.queue else True


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = MyQueue()
    sol_obj.push(1)
    sol_obj.push(2)
    # sol_obj.push(3)
    print(sol_obj.peek())
    print(sol_obj.pop())
    print(sol_obj.empty())
    # print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

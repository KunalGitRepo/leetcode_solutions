import time


class MyStack:

    def __init__(self):
        self.stack = list()

    def push(self, x: int) -> None:
        return self.stack.insert(0, x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def top(self) -> int:
        top_val = self.stack[0] if self.stack else None
        return top_val

    def empty(self) -> bool:
        is_empty = False if self.stack else True
        return is_empty


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = MyStack()
    sol_obj.push(1)
    sol_obj.push(2)
    print(sol_obj.top())
    print(sol_obj.pop())
    print(sol_obj.empty())

    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)
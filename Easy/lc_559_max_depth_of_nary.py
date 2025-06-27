import time
from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        max_depth = 1
        if not root:
            return 0
        if root.children:
            depth, max_depth = self.max_depth(node=root, depth=depth, max_depth=max_depth)
        elif root:
            max_depth = 1
        else:
            max_depth = 0
        return max_depth

    def max_depth(self, node, depth, max_depth):
        depth += 1
        if node.children:
            # if isinstance(node.children, list):
            for n in node.children:
                depth, max_depth = self.max_depth(node=n, depth=depth, max_depth=max_depth)
                max_depth = depth if depth > max_depth else max_depth

        max_depth = depth if depth > max_depth else max_depth
        depth -= 1
        return depth, max_depth


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    child6 = Node(6)
    child5 = Node(5)
    child3 = Node(3, children=[child5, child6])

    child8 = Node(8)
    child10 = Node(10)
    child11 = Node(11)
    child13 = Node(13)
    child12 = Node(12, children=[child13])
    child9 = Node(9, children=[child10, child11, child12])
    child7 = Node(7, children=[child8, child9])
    child4 = Node(4)
    child2 = Node(2, children=[child7])
    # child4 = Node(4)
    node1 = Node(1, children=[child2, child3, child4])

    node1 = None

    ret_val = sol_obj.maxDepth(root=node1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

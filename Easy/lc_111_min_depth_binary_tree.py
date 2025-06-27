import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_last_node(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = self.find_depth(node=root)
        return depth

    def find_depth(self, node, depth=9999, curr_depth=1):
        if node.left or node.right:
            if node.left:
                curr_depth += 1
                depth = self.find_depth(node=node.left, depth=depth, curr_depth=curr_depth)
                curr_depth -= 1
            if node.right:
                curr_depth += 1
                depth = self.find_depth(node=node.right, depth=depth, curr_depth=curr_depth)
                curr_depth -= 1
        else:
            depth = curr_depth if curr_depth < depth else depth
        return depth


if "__main__" == __name__:
    start_time = time.time()
    root = TreeNode(val=1,
                    left=TreeNode(2,
                                  left=TreeNode(4,
                                                left=TreeNode(8),
                                                right=TreeNode(9)),
                                  right=TreeNode(5,
                                                 left=TreeNode(10))),
                    right=TreeNode(3,
                                   left=TreeNode(6),
                                   right=TreeNode(7)))
    sol_obj = Solution()
    ret_val = sol_obj.find_last_node(root=root)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

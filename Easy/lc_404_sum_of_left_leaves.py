import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0

        sum = self.sum_of_left_leaves(root, 0, False)
        return sum

    def sum_of_left_leaves(self, node, sum, left_flag):
        if not node.left and not node.right:
            if left_flag:
                sum += node.val
                return sum
        if node.left:
            sum = self.sum_of_left_leaves(node.left, sum, True)

        if node.right:
            sum = self.sum_of_left_leaves(node.right, sum, False)

        return sum


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    node1 = TreeNode(5,
                     left=TreeNode(4),
                     right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))
    node1 = TreeNode(2,
                     right=TreeNode(1))
    # node1 = TreeNode(1,
    #                  left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
    #                  right=TreeNode(3, left=TreeNode(6, left=TreeNode(2))))
    ret_val = sol_obj.sumOfLeftLeaves(root=node1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, targetSum, 0)

    def dfs(self, node, target_sum, sum_total):
        sum_total += node.val
        if not node.left and not node.right:
            return True if sum_total == target_sum else False

        if node.left:
            if self.dfs(node.left, target_sum, sum_total):
                return True
        if node.right:
            if self.dfs(node.right, target_sum, sum_total):
                return True
        return False


if "__main__" == __name__:
    start_time = time.time()
    root = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(11)
    node4 = TreeNode(7)
    node5 = TreeNode(2)
    node6 = TreeNode(8)
    node7 = TreeNode(13)
    node8 = TreeNode(4)
    node9 = TreeNode(1)
    root.left = node2
    root.right = node6
    node2.left = node3
    node3.left = node4
    node3.right = node5
    node6.left = node7
    node6.right = node8
    node8.right = node9
    # root = TreeNode()
    sol_obj = Solution()
    target = 18
    ret_val = sol_obj.hasPathSum(root, target)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)
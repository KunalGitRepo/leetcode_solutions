import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        deep = self.dfs(root, 0, 0)
        return deep + 1

    def dfs(self, node, depth, count):
        count += 1
        if node.left or node.right:
            if count > depth:
                depth = count
        if node.left:
            depth = self.dfs(node.left, depth, count)
        if node.right:
            depth = self.dfs(node.right, depth, count)
        count -= 1
        return depth


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
    # node2.left = node3
    # node3.left = node4
    # node3.right = node5
    node6.left = node7
    node6.right = node8
    node8.right = node9
    sol_obj = Solution()
    ret_val = sol_obj.maxDepth(root)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

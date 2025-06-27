import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        current_depth, highest_depth = self.tree_paths(node=root, left_depth=0, right_depth=0, highest_depth=0)
        return highest_depth

    def tree_paths(self, node, left_depth, right_depth, highest_depth):

        if not node.right and not node.left:
            current_depth = left_max + right_max
            highest_depth = current_depth if current_depth > highest_depth else highest_depth
            return left_depth, right_depth, highest_depth

        if node.left:
            left_max += 1
            left_curr += 1
            left_depth, right_depth, highest_depth = self.tree_paths(node=node.left, left_depth=left_depth, right_depth=right_depth, highest_depth=highest_depth)
            left_curr -= 1

        if node.right:
            right_max += 1
            right_curr += 1
            left_depth, right_depth, highest_depth = self.tree_paths(node=node.right, left_depth=left_depth, right_depth=right_depth, highest_depth=highest_depth)
            right_curr -= 1

        return left_depth, right_depth, highest_depth


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    node1 = TreeNode(5,
                     left=TreeNode(4),
                     right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))
    # node1 = TreeNode(5,
    #                  left=TreeNode(4, left=TreeNode(6)))
    node1 = TreeNode(1,
                     left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                     right=TreeNode(3, left=TreeNode(6, right=TreeNode(9)), right=TreeNode(7)))
    # node1 = None
    ret_val = sol_obj.binaryTreePaths(root=node1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

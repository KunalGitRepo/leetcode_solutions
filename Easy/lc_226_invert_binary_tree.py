import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if not root.left and not root.right:
            return root
        self.invert_tree(node=root)
        return root

    def invert_tree(self, node):
        if node.left and node.right:
            node.left, node.right = node.right, node.left
        elif node.left and not node.right:
            node.right = node.left
            node.left = None
        elif not node.left and node.right:
            node.left = node.right
            node.right = None
        if node.left:
            self.invert_tree(node=node.left)
        if node.right:
            self.invert_tree(node=node.right)
        return True


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    node1 = TreeNode(5,
                     left=TreeNode(4),
                     right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))
    node1 = TreeNode(5,
                     left=TreeNode(4, left=TreeNode(6)))
    # node1 = TreeNode(1,
    #                  left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
    #                  right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))
    node1 = None
    ret_val = sol_obj.invertTree(root=node1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

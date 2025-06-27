import time
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        ret_val = False
        if root.left and root.right:
            ret_val = self.validate_symmetry(root.left, root.right, True)
        elif not root.left and not root.right:
            return True
        elif (root.left and not root.right) or (not root.left and root.right):
            return False
        return ret_val

    def validate_symmetry(self, left, right, ret_val):
        if not ret_val:
            return ret_val
        if left.val != right.val:
            ret_val = False
            return ret_val

        if left.left and right.right:
            ret_val = self.validate_symmetry(left.left, right.right, ret_val)
        elif (left.left and not right.right) or (not left.left and right.right):
            ret_val = False
            return ret_val

        if left.right and right.left:
            ret_val = self.validate_symmetry(left.right, right.left, ret_val)
        elif (left.right and not right.left) or (not left.right and right.left):
            ret_val = False
            return ret_val

        return ret_val


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    node1 = TreeNode(1,
                     left=TreeNode(2, left=TreeNode(3)),
                     right=TreeNode(2, left=TreeNode(3)))
    ret_val = sol_obj.isSymmetric(root=node1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

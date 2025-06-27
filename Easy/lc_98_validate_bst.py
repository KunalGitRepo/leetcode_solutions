import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        ret_val = True
        if root.left or root.right:
            ret_val = self.validate_bst(root, True, None)
        elif not root.left and not root.right:
            return True
        # elif root.left and not root.right:
        #     if root.val <= root.left.val:
        #         return False
        # elif not root.left and root.right:
        #     if root.val >= root.right.val:
        #         return False

        return ret_val

    def validate_bst(self, node, ret_val, last_num):
        if not ret_val:
            return ret_val

        if node.left:
            if node.val <= node.left.val:
                ret_val = False
                return ret_val
            else:
                ret_val = self.validate_bst(node=node.left, ret_val=ret_val, last_num=last_num)

        if last_num != None:
            if last_num > node.val:
                ret_val = False
                return ret_val

        last_num = node.val

        if node.right:
            if node.val >= node.right.val:
                ret_val = False
                return ret_val
            else:
                ret_val = self.validate_bst(node=node.right, ret_val=ret_val, last_num=last_num)

        return ret_val


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    node1 = TreeNode(5,
                     left=TreeNode(4),
                     right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))
    # node1 = TreeNode(2,
    #                  left=TreeNode(1),
    #                  right=TreeNode(3))
    node1 = TreeNode(3,
                     right=TreeNode(30, left=TreeNode(10, right=TreeNode(15, right=TreeNode(45)))))
    ret_val = sol_obj.isValidBST(root=node1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

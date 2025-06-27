import time
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        val = True
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False

        if p.val != q.val:
            return False

        if p.left and q.left:
            val = self.isSameTree(p=p.left, q=q.left)
        elif (p.left and not q.left) or (not p.left and q.left):
            return False

        if val:
            if p.right and q.right:
                val = self.isSameTree(p=p.right, q=q.right)
            elif (p.right and not q.right) or (not p.right and q.right):
                return False

        return val


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(1)
    node1 = None
    ret_val = sol_obj.isSameTree(p=node1, q=node2)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)
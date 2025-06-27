import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if not root.left and not root.right:
            return root
        self.invert_tree(node=[root], odd=False)
        return root

    def invert_tree(self, node, odd):
        node_dict = dict()
        count = 1
        if node.left and node.right:
            node_dict[count] = node.left
            node_dict[count] = node.right
        elif node.left and not node.right:
            node_dict[count] = node.left
        elif not node.left and node.right:
            node_dict[count] = node.right

        return True


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    node1 = TreeNode(5,
                     left=TreeNode(4),
                     right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))
    node1 = TreeNode(5,
                     left=TreeNode(4, left=TreeNode(6)))
    node1 = TreeNode(1,
                     left=TreeNode(2,
                                   left=TreeNode(4, left=TreeNode(8), right=TreeNode(9)),
                                   right=TreeNode(5, left=TreeNode(10), right=TreeNode(11))),
                     right=TreeNode(3,
                                    left=TreeNode(6, left=TreeNode(12), right=TreeNode(13)),
                                    right=TreeNode(7, left=TreeNode(14), right=TreeNode(15))))
    # node1 = None
    ret_val = sol_obj.reverseOddLevels(root=node1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

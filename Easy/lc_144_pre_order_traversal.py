import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node_list = list()

        if not root:
            return node_list

        if not root.left and not root.right:
            node_list.append(root.val)
        else:
            node_list = self.traverse(root, [])

        return node_list

    def traverse(self, node, node_list):

        node_list.append(node.val)

        if node.left:
            self.traverse(node.left, node_list)

        if node.right:
            self.traverse(node.right, node_list)
        return node_list


if "__main__" == __name__:
    start_time = time.time()
    sol_obj = Solution()
    node1 = TreeNode(1,
                     left=TreeNode(2, left=TreeNode(3), right=TreeNode(6)),
                     right=TreeNode(4, left=TreeNode(5)))
    node1 = TreeNode(1,
                     right=TreeNode(0, left=TreeNode(3)))
    ret_val = sol_obj.inorderTraversal(root=node1)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

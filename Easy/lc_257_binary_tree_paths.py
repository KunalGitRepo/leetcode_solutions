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
            return [""]
        if not root.left and not root.right:
            return [str(root.val)]
        path_list, node_path_list = self.tree_paths(node=root, path_list=[], node_path_list=[str(root.val)])
        return path_list

    def tree_paths(self, node, path_list, node_path_list):

        if not node.right and not node.left:
            node_path_str = '->'.join(node_path_list)
            path_list.append(node_path_str)
            node_path_list.pop(-1)
            return path_list, node_path_list

        if node.left:
            node_path_list.append(str(node.left.val))
            path_list, node_path_list = self.tree_paths(node=node.left, path_list=path_list, node_path_list=node_path_list)

        if node.right:
            node_path_list.append(str(node.right.val))
            path_list, node_path_list = self.tree_paths(node=node.right, path_list=path_list, node_path_list=node_path_list)

        node_path_list.pop(-1)
        return path_list, node_path_list


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

import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # node_count = self.bfs([root])
        leafs, depth = self.dfs(root)
        node_count = (2 ** (depth)) - 1
        return node_count + leafs

    def dfs(self, node, depth=0, curr_depth=0, leaf_node=0):
        # depth = curr_depth if curr_depth > depth else depth

        if curr_depth > depth:
            depth = curr_depth

        if not node.right and not node.left:
            if curr_depth == depth:
                # node_count = (2 ** (depth)) - 1
                leaf_node += 1
            # leaf_node = leaf_node + 1 if curr_depth == depth else leaf_node
            return leaf_node, depth

        if node.left:
            curr_depth += 1
            leaf_node, depth = self.dfs(node=node.left, depth=depth, curr_depth=curr_depth, leaf_node=leaf_node)
            curr_depth -= 1

        if node.right:
            curr_depth += 1
            leaf_node, depth = self.dfs(node=node.right, depth=depth, curr_depth=curr_depth, leaf_node=leaf_node)
            curr_depth -= 1

        return leaf_node, depth

    # def bfs(self, node_list):
    #     node_count = 0
    #     while node_list:
    #         node_count += 1
    #         if node_list[0].left:
    #             node_list.append(node_list[0].left)
    #         if node_list[0].right:
    #             node_list.append(node_list[0].right)
    #         node_list.pop(0)
    #     return node_count


if "__main__" == __name__:
    start_time = time.time()
    root = TreeNode(val=1,
                    left=TreeNode(2,
                                  left=TreeNode(4,
                                                left=TreeNode(8),
                                                right=TreeNode(9)),
                                  right=TreeNode(5,
                                                 left=TreeNode(10),
                                                 right=TreeNode(11))),
                    right=TreeNode(3,
                                   left=TreeNode(6,
                                                 left=TreeNode(12)),
                                   right=TreeNode(7)))
    sol_obj = Solution()
    ret_val = sol_obj.countNodes(root=root)
    print(ret_val)
    time_taken = time.time() - start_time
    print("Execution time : %s" % time_taken)

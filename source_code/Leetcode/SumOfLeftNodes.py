# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root:[TreeNode]) -> int:
        tot_sum = 0
        if not root:
            return 0
        nodes = [root]

        while nodes:
            current_node = nodes.pop(0)

            if current_node.left and not current_node.left.left and not current_node.left.right:
                tot_sum += current_node.left.val
            if current_node.left:
                nodes.append(current_node.left)
            if current_node.right:
                nodes.append(current_node.right)

        return tot_sum


# if __name__ == "__main__":
#
#     root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
#
#     sol = Solution()
#     result = sol.sumOfLeftLeaves(root)
#     print(result) - Uncomment it to Run.
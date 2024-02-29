from collections import deque  #


# A binary tree is named Even-Odd if it meets the following conditions:
#
# The root of the binary tree is at level index 0, its children are at level index 1, their children are at level
# index 2, etc. For every even-indexed level, all nodes at the level have odd integer values in strictly increasing
# order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in
# strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is
# Even-Odd, otherwise return false.
#
#
#
# Example 1:
#
#
# Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
# Output: true
# Explanation: The node values on each level are:
# Level 0: [1]
# Level 1: [10,4]
# Level 2: [3,7,9]
# Level 3: [12,8,6,2]
# Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.


# CODE:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: [TreeNode]) -> bool:
        nodequeue = deque([root])

        def isValid(level, num):
            if level % 2 == 0:
                return num % 2 != 0
            else:
                return num % 2 == 0

        level = 0

        while nodequeue:
            previousValue = None

            for i in range(len(nodequeue)):
                currentNode = nodequeue.popleft()

                if not isValid(level, currentNode.val):
                    return False

                if previousValue is not None:
                    if level % 2 == 0 and previousValue >= currentNode.val:
                        return False
                    elif level % 2 != 0 and previousValue <= currentNode.val:
                        return False

                previousValue = currentNode.val
                # print(f"Previous value after processing node with value {currentNode.val}: {previousValue}")

                if currentNode.left:
                    nodequeue.append(currentNode.left)
                if currentNode.right:
                    nodequeue.append(currentNode.right)

            level += 1
            # print(f"Level after processing all nodes in the current level: {level}")

        return True

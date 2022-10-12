# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = list()
        stack = deque()
        node = root
        while len(stack) != 0 or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node)
            node = node.right

        size = len(result)
        index = 0
        while index + 1 < size:
            result[index].right = result[index + 1]
            result[index].left = None
            result[index + 1].left = None
            index += 1
        return result[0]

    result = None
    def increasingBST1(self, root: TreeNode) -> TreeNode:
        self.dumpNode = TreeNode(-1)
        self.result = self.dumpNode
        def inOrder(root: TreeNode):
            if root:
                inOrder(root.left)
                if self.result is None:
                    self.result = root
                self.dumpNode.right = root
                root.left = None
                self.dumpNode = root
                inOrder(root.right)

        inOrder(root)
        return self.result.right


if __name__ == "__main__":
    right22 = TreeNode(7)
    left21 = TreeNode(6)
    right12 = TreeNode(5)
    left11 = TreeNode(4)
    right1 = TreeNode(3, left21, right22)
    left1 = TreeNode(2, left11, right12)
    root = TreeNode(1, left1, right1)
    # right11 = TreeNode(3)
    # left1 = TreeNode(1)
    # right1 = TreeNode(4, right11)
    # root = TreeNode(2, left1, right1)
    bst = Solution().increasingBST1(root)
    print(bst)

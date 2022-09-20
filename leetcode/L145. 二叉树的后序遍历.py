# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        def inOrder(root):
            if root is None:
                return
            inOrder(root.left)
            inOrder(root.right)
            result.append(root.val)
        inOrder(root)
        return result

    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        stack = deque()
        while root or stack:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.right
            root = stack.pop()
            root = root.left
        result.reverse()
        return result


if __name__ == "__main__":
    # left21 = TreeNode(3)
    # right1 = TreeNode(2, left21)
    # root = TreeNode(1, None, right1)
    right22 = TreeNode(7)
    left21 = TreeNode(6)
    right12 = TreeNode(5)
    left11 = TreeNode(4)
    right1 = TreeNode(3, left21, right22)
    left1 = TreeNode(2, left11, right12)
    root = TreeNode(1, left1, right1)
    # result = Solution().postorderTraversal(root)
    result = Solution().postorderTraversal1(root)
    print(result)
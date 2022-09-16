# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


# 前序遍历 [1,None,2,3]
# 中序遍历 [1,3,2]
# 后序遍历 [3,None,2,1]

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def midOrder(node: TreeNode):
            if node == None:
                return node
            midOrder(node.left)
            result.append(node.val)
            midOrder(node.right)

        result = list()
        midOrder(root)
        return result

    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        stack = deque()
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
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
    # result = Solution().inorderTraversal(root)
    result = Solution().inorderTraversal1(root)
    print(result)

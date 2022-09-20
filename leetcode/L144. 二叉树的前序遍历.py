# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


# 莫里斯算法
# https://baijiahao.baidu.com/s?id=1712736660249781959&wfr=spider&for=pc


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node: TreeNode):
            if node:
                left = node.left
                right = node.right
                print(node.val)
                result.append(node.val)
                preorder(left)
                preorder(right)

        result = []
        preorder(root)
        return result

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        stack = deque()
        while root or stack:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left

            root = stack.pop()
            root = root.right
        return result

    def morris(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        mostRight = None
        if not root:
            return result
        cur = root
        while cur:
            mostRight = cur.left
            if mostRight:
                while mostRight.right and mostRight != cur:
                    mostRight = mostRight.right
                if mostRight.right == None:
                    mostRight.right = cur
                    cur = cur.left
                    continue
                else:
                    mostRight.right = None
            cur = cur.right


if __name__ == "__main__":
    root = TreeNode()
    root.val = 1
    left1 = TreeNode()
    left1.val = 2
    right1 = TreeNode()
    right1.val = 3
    left11 = TreeNode()
    left11.val = 4
    right12 = TreeNode()
    right12.val = 5
    left21 = TreeNode()
    left21.val = 6
    right22 = TreeNode()
    right22.val = 7
    root.left = left1
    root.right = right1
    left1.left = left11
    left1.right = right12
    right1.left = left21
    right1.right = right22
    # Solution().preorderTraversal(root)
    result = Solution().preorderTraversal2(root)
    # result = Solution().morris(root)
    print(result)

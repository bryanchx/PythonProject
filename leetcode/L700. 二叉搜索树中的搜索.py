# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.target = None
        self.val = val

        def midOrder(root: TreeNode):
            if root is None:
                return
            midOrder(root.left)
            if root.val == self.val:
                self.target = root
                return
            midOrder(root.right)

        midOrder(root)
        return self.target

    def searchBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:
            return root
        return self.searchBST(root.left if root.val > val else root.right, val)

    def searchBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None:
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
            else:
                return root
        return None



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
    bst = Solution().searchBST2(root, 2)
    print(bst)

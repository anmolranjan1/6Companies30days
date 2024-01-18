from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class T:
    def __init__(self, isBST=False, max_val=float('-inf'), min_val=float('inf'), sum_val=0):
        self.isBST = isBST
        self.max = max_val
        self.min = min_val
        self.sum = sum_val

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        self.traverse(root, ans)
        return ans[0]

    def traverse(self, root: Optional[TreeNode], ans: list) -> T:
        if root is None:
            return T(True, float('-inf'), float('inf'), 0)

        left = self.traverse(root.left, ans)
        right = self.traverse(root.right, ans)

        if not left.isBST or not right.isBST or (root.left and root.val <= left.max) or (root.right and root.val >= right.min):
            return T()

        # The `root` is a valid BST.
        curr_sum = root.val + left.sum + right.sum
        ans[0] = max(ans[0], curr_sum)

        return T(True, max(root.val, right.max), min(root.val, left.min), curr_sum)

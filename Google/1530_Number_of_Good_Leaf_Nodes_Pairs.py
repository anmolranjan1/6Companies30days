# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = [0]

        def dfs(root, distance, ans):
            d = [0] * (distance + 1)  # {distance: the number of leaf nodes}
            if not root:
                return d
            if not root.left and not root.right:
                d[0] = 1
                return d

            dl = dfs(root.left, distance, ans)
            dr = dfs(root.right, distance, ans)

            for i in range(distance):
                for j in range(distance):
                    if i + j + 2 <= distance:
                        ans[0] += dl[i] * dr[j]

            for i in range(distance):
                d[i + 1] = dl[i] + dr[i]

            return d

        dfs(root, distance, ans)
        return ans[0]

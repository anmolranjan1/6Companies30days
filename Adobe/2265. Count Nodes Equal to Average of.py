class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.matchCount = 0
        
        self.explore(root)
        
        return self.matchCount
    
    def explore(self, root):
        if root is None:
            return 0, 0
        
        ls, lc = self.explore(root.left)
        rs, rc = self.explore(root.right)
        
        childTotal = ls + rs + root.val
        childCount = lc + rc + 1
        
        if childCount != 0 and root.val == childTotal // childCount:
            self.matchCount += 1
        
        return childTotal, childCount
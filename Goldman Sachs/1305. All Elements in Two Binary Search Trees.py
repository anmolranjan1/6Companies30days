import heapq
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def gen(node):
            if node:
                yield from gen(node.left)
                yield node.val
                yield from gen(node.right)
        return list(heapq.merge(gen(root1), gen(root2)))
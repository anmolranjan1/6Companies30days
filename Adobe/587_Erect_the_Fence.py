from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        hull = []

        trees.sort(key=lambda x: (x[0], x[1]))

        for tree in trees:
            while len(hull) > 1 and cross(hull[-1], hull[-2], tree) > 0:
                hull.pop()
            hull.append(tree)

        hull.pop()
        for i in range(len(trees) - 1, -1, -1):
            while len(hull) > 1 and cross(hull[-1], hull[-2], trees[i]) > 0:
                hull.pop()
            hull.append(trees[i])

        hull.sort(key=lambda x: (x[0], x[1]))
        hull = list({tuple(x) for x in hull})

        return hull

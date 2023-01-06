class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n, a = {}, defaultdict(list)
        def can(b):
            for init in (True, False): n[b] = False if init else all(n[d] if d in n else can(d) for d in a[b] if d in a)
            return n[b]
        return any(a.update({b:a[b] + [d]}) for b, d in prerequisites) or all(can(b) for b in a)
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:     
        n, m = len(students), len(students[0])
        out = []
        def dfs(i, used, score):           
            if i == n:
                out.append(score)
                return           
            for mentor in range(n):
                if str(mentor) not in used:
                    curr = sum(a==b for a, b in zip(students[i], mentors[mentor]))
                    dfs(i+1, used+str(mentor), score+curr)
            
        dfs(0, '', 0)
        return max(out)
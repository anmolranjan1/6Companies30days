class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        a = 0 
        b=  {} 
        c = 0
        for r, f in enumerate(fruits):
            b[f] = b.get(f, 0)+1 
            while len(b) > 2: 
                cur = fruits[c]
                b[cur] -= 1
                if b[cur] ==0:
                    b.pop(cur) 
                c += 1
            a = max(a, r-c+1)
        return a
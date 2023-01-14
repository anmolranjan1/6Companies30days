class Solution:
    def findIntegers(self, n: int) -> int:
        fn = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269]
        nstr = bin(n)[2:]
        p = nstr.find('11')
        tmp = list(nstr)
        if p >= 0:
            for i in range(p + 1, len(tmp)):
                tmp[i] = '10'[(i - p) % 2]       
        max_n = ''.join(tmp)
        ans = fn[len(max_n) - 1] + 1
        for i in range(2, len(max_n)):
            if max_n[i] == '1':
                ans += fn[len(max_n) - i - 1]
        
        return 
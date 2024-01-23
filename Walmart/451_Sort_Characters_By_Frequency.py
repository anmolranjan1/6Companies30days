class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        ans = ""
        count = [0] * 128

        buckets = [[] for _ in range(n + 1)]

        for c in s:
            count[ord(c)] += 1

        for i in range(128):
            freq = count[i]
            if freq > 0:
                buckets[freq].append(chr(i))

        for freq in range(n, 0, -1):
            for c in buckets[freq]:
                ans += freq * c

        return ans

class Solution:
  def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
    ans = []
    indicesA = self._kmp(s, a)
    indicesB = self._kmp(s, b)
    indicesBIndex = 0

    for i in indicesA:
      while indicesBIndex < len(indicesB) and indicesB[indicesBIndex] - i < -k:
        indicesBIndex += 1
      if indicesBIndex < len(indicesB) and indicesB[indicesBIndex] - i <= k:
        ans.append(i)

    return ans

  def _kmp(self, s: str, pattern: str) -> List[int]:
    def getLPS(s: str) -> List[int]:
      lps = [0] * len(s)
      j = 0
      for i in range(1, len(s)):
        while j > 0 and s[j] != s[i]:
          j = lps[j - 1]
        if s[i] == s[j]:
          lps[i] = j + 1
          j += 1
      return lps

    lps = getLPS(pattern)
    res = []
    i = 0
    j = 0
    while i < len(s):
      if s[i] == pattern[j]:
        i += 1
        j += 1
      if j == len(pattern):
        res.append(i - j)
        j = lps[j - 1]
      elif i < len(s) and s[i] != pattern[j]:
        if j != 0:
          j = lps[j - 1]
        else:
          i += 1
    return res
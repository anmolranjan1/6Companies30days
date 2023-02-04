class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = len(nums1), len(nums2)
        memo = [0]*(s1+1)*(s2+1)
        for i in range(s1-1, -1, -1):
            for j in range(s2-1, -1, -1):
                if nums1[i] == nums2[j]:
                    if s1 < s2:
                        memo[(s1+1)*i+j] = memo[(s1+1)*(i+1)+(j+1)]+1
                    else:
                        memo[(s2+1)*i+j] = memo[(s2+1)*(i+1)+(j+1)]+1
        return max(memo)
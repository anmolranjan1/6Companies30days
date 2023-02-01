class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        pref_sum,l,s,sol=list(accumulate(nums2:=[int(x%p==0) for x in nums])),len(nums),set(),0
        for left,x in enumerate(pref_sum):
            for end in range(left+1,bisect_left(pref_sum,x+k if nums2[left] else x+1+k ,lo=left)+1):
                if (t:=tuple(nums[left:end])) not in s:s.add(t)
        return len(s)
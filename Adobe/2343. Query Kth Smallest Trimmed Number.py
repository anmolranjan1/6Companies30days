class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        n = len(nums)
        for k, trim in queries:
            trimmed_array = [[elem[-trim:],i] for i, elem in enumerate(nums)]
            trimmed_array.sort()
            res.append(trimmed_array[k - 1][1])           
        return res
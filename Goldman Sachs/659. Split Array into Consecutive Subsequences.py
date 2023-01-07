class Solution:
    def isPossible(self, nums: List[int]) -> bool:       
        a = defaultdict(int)    
        b = Counter(nums)               
        for num in nums:
            if (not b[num]): 
                continue              
            if (a[num-1] > 0):   
                a[num-1] -= 1 
                a[num] += 1
                b[num] -= 1               
            else:   
                if (not b[num+1] or not b[num+2]):  
                    return False
                b[num] -= 1
                b[num+1] -= 1
                b[num+2] -= 1
                a[num+2] += 1        
        return True
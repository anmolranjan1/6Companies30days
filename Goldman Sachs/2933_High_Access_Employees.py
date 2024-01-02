from typing import List
from collections import defaultdict

class Solution:
    def is_high_access(self, times):
        n = len(times)
        
        for i in range(2, n):
            curr_time = times[i]
            prev_prev = times[i - 2]
            if prev_prev + 99 >= curr_time:
                return True
        return False
    
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        ans = []
        map_ = defaultdict(list)
        
        for curr in access_times:
            emp = curr[0]
            time = curr[1]
            
            t = int(time)
            map_[emp].append(t)
        
        for emp, times in map_.items():
            times.sort()
            if self.is_high_access(times):
                ans.append(emp)
        
        return ans
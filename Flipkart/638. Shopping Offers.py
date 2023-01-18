class Solution:
	def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
		@lru_cache(None)
		def dfs(k,need):
			need = list(need)
			ans =0
			for i in range(len(need)):
				ans += price[i]*need[i]
			for i in range(k,len(special)):
				offer = special[i]
				check = True
				for a in range(len(need)):
					need[a] -= offer[a]
					if need[a] < 0:
						check = False
				if check:
					ans = min(ans,offer[-1] + dfs(i,tuple(need)))

				for a in range(len(needs)):
					need[a] += offer[a]
			return ans
		return dfs(0,tuple(needs))
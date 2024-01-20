from typing import List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        return self.dfs(price, special, needs, 0)

    def dfs(self, price, special, needs, s):
        ans = 0
        for i in range(len(price)):
            ans += price[i] * needs[i]

        for i in range(s, len(special)):
            if self.isValid(special[i], needs):
                # Use the special[i].
                for j in range(len(needs)):
                    needs[j] -= special[i][j]
                ans = min(ans, special[i][-1] + self.dfs(price, special, needs, i))
                # Unuse the special[i] (backtracking).
                for j in range(len(needs)):
                    needs[j] += special[i][j]

        return ans

    # Returns true if this special offer is a valid one.
    def isValid(self, offer, needs):
        for i in range(len(needs)):
            if needs[i] < offer[i]:
                return False
        return True

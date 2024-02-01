from typing import List

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dead = set()
        self.family = {}
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.family:
            self.family[parentName] = []
        self.family[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        self.dfs(self.kingName, ans)
        return ans

    def dfs(self, name: str, ans: List[str]) -> None:
        if name not in self.dead:
            ans.append(name)
        if name not in self.family:
            return

        for child in self.family[name]:
            self.dfs(child, ans)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
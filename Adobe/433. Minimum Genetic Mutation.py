class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        dic=defaultdict(lambda :0)
        lst=[[start,0]]
        dic[start]=1
        while lst:
            x,d=lst.pop(0)
            if x==end:
                return d
            for i in range(len(bank)):
                ct=0
                for j in range(8):
                    if x[j]!=bank[i][j]:
                        ct+=1
                if ct==1:
                    if dic[bank[i]]==0:
                        lst.append([bank[i],d+1])
                        dic[bank[i]]=1
        return -1
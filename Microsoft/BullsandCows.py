class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b=c=0
        bf=[0 for i in range(10)]
        cf=[0 for i in range(10)]
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                b+=1
            else:
                bf[int(secret[i])]+=1
                cf[int(guess[i])]+=1
        for i in range(10):
            c+=min(bf[i],cf[i])
        return  str(b)+"A"+str(c)+"B"
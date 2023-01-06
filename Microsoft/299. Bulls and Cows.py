class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a=0
        for i,j in zip(secret,guess):
            if (i==j):
                a+=1
        k=Counter(secret)
        l=Counter(guess)
        return "%dA%dB" % (a, sum((k & l).values()) - a)
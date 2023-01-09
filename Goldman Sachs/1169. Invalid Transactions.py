class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        a = sorted([i.split(',') for i in transactions], key=lambda i: (i[0],int(i[1])))
        b = [False]*len(a)
        for i in range(len(a)):
            if int(a[i][2]) > 1000:
                b[i] = True
            j = i + 1
            while j < len(a) and a[j][0] == a[i][0] and int(a[j][1]) - int(a[i][1]) <= 60:
                if a[j][3] != a[i][3]:
                    b[i] = True
                    b[j] = True
                j += 1   
        return [','.join(a[i]) for i in range(len(a)) if b[i]]
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # friends[i] := True if i-th friend is left
        friends = [False] * n

        friendCount = n
        fp = 0  # friends' index

        while friendCount > 1:
            for i in range(k):
                while friends[fp % n]:  # The friend is not there.
                    fp += 1              # Point to the next one.
                fp += 1

            friends[(fp - 1) % n] = True
            friendCount -= 1

        winner_index = friends.index(False)
        return winner_index + 1

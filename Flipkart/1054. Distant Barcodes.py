class Solution:
    def rearrangeBarcodes(self, B: List[int]) -> List[int]:
        L, C = len(B), collections.Counter(B)
        B.sort(key = lambda x: (C[x],x))
        B[1::2], B[::2] = B[:L//2], B[L//2:]
        return B
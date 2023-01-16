class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        tot_sum = 0
        neg_nums, min_val = 0, float('inf')
        for row in matrix:
            for col_val in row:
                tot_sum += abs(col_val)
                min_val = min(min_val, abs(col_val))
                if col_val < 0:
                    neg_nums += 1
        if neg_nums % 2 == 0:
            return tot_sum
        else:
            return tot_sum - 2*min_val
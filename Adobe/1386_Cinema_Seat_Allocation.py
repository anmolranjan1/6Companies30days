class Solution:
  def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    ans = 0
    rowToSeats = collections.Counter()

    for row, seat in reservedSeats:
      rowToSeats[row] |= 1 << (seat - 1)

    for seats in rowToSeats.values():
      if (seats & 0b0111111110) == 0:
        ans += 2
      elif (seats & 0b0111100000) == 0 \
              or (seats & 0b0001111000) == 0 \
              or (seats & 0b0000011110) == 0:
        ans += 1

    return ans + (n - len(rowToSeats)) * 2
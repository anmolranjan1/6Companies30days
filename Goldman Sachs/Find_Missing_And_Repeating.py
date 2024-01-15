class Solution:
    def findTwoElement(self, arr, n):
        repeating = 0
        missing = 0

        # Marking the elements in the array
        for i in range(n):
            index = abs(arr[i]) - 1
            if arr[index] > 0:
                arr[index] = -arr[index]
            else:
                repeating = abs(arr[i])

        # Finding the missing element
        for i in range(n):
            if arr[i] > 0:
                missing = i + 1
                break

        return [repeating, missing]
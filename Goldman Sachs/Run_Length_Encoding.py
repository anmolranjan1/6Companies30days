def encode(arr):
    result = ""
    count = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            result += arr[i - 1] + str(count)
            count = 1
    
    result += arr[-1] + str(count)
    
    return result
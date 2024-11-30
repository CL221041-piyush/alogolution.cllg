def findEquilibriumIndex(arr):
    n = len(arr)
    total_sum = sum(arr)  
    left_sum = 0 

    for i in range(n):
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            return i + 1  
        
        left_sum += arr[i]

    return -1

arr = [-7, 1, 5, 2, -4, 3, 0]
print(findEquilibriumIndex(arr))  

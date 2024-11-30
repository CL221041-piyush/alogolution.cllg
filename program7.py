def maxSumSubarray(arr, n, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum  
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]  
        max_sum = max(max_sum, window_sum)  
    
    return max_sum

#example1
arr1 = [100, 200, 300, 400]
k1 = 2
print(maxSumSubarray(arr1, len(arr1), k1))  
#example2
arr2 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k2 = 4
print(maxSumSubarray(arr2, len(arr2), k2))  

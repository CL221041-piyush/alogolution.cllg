def maxSubArrayLen(nums, target):
    prefix_sum_map = {0: -1}  
    prefix_sum = 0  
    max_len = 0  

    for i, num in enumerate(nums):
        prefix_sum += num
        
        if prefix_sum - target in prefix_sum_map:
            max_len = max(max_len, i - prefix_sum_map[prefix_sum - target])
        
        if prefix_sum not in prefix_sum_map:
            prefix_sum_map[prefix_sum] = i
    
    return max_len

nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target = 8
print(maxSubArrayLen(nums, target))  

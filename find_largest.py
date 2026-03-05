def find_largest(nums):
    largest = nums[0]
    for numbers in nums:
        if numbers > largest:
            largest = numbers
        
    return largest
        
print(find_largest([1,3,200,23,12]))

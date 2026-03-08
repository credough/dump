def find_smallest(nums):
  smallest = nums[0]
  for n in nums:
    if n < smallest:
      smallest = n

    return smallest
    
print(find_smallest([22,33,47,54,26,28]))

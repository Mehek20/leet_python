def twosums(nums, target):
    nums_to_index={}
    for index, num in enumerate(nums):
        compliment=target-num
        if compliment in nums_to_index:
            return [nums_to_index[compliment],index]
        nums_to_index[num] = index
        print(nums_to_index)
        
nums1 = [2, 7, 11, 15]
target1 = 9
print(twosums(nums1, target1))
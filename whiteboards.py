# 9/20/22

# Given an array of integers (nums), which is sorted in ascending order, and a target integer, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

nums1 = [-1, 0, 3, 5, 9, 12]

target = 9
target2 = 2

def find_index(nums, target):
    for i in nums:
        if i == target:
            return nums.index(i)
        elif i > target:
            return -1
    
print(find_index(nums1, 2))
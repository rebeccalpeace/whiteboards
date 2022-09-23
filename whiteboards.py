# 9/20/22

# Given an array of integers (nums), which is sorted in ascending order, and a target integer, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# nums1 = [-1, 0, 3, 5, 9, 12]

# target = 9
# target2 = 2

# def find_index(nums, target):
#     for i in nums:
#         if i == target:
#             return nums.index(i)
#         elif i > target:
#             return -1
    
# print(find_index(nums1, 2))


# def isAnagram(s, t):
#     return sorted(s) == sorted(t)

# print(isAnagram('rat', 'car'))



# Nate's workshop 9/23/22

# function accepts a string
# If string is a number, return string as an integer.
# Ignore/remove any spaces from beginning of string
# If first character of the number is "-", return as a negative integer
# If first character is a "+", return as a positive integer
# If string represents integer that is larger than max 32-bit signed integer, return largest possible 32-bit integer.
# If string represents an integer that is smaller than the minium 32-bit signed integer, return smallest possible 32-bit integer.
# If string is not a number, return 0.
# if no +/- prefix, assume positive

# Test cases
# s = "12"
# s = "    12 "
# s = "   -12 "
# s = "-12"
# s = " +12"
# s = "hello world" #0
# s = "-2147483650" # -2147483648
# s = "+2147483650" # 2147483647
# s = "    "

# def str_to_int(s):
#     direction = True
#     new = s.strip() # O(n) T + S
#     if not new:
#         return 0
#     if new[0] == '+' or new[0] == '-':
#         if new[0] == '-':
#             direction = False
#         new = new[1:]  # O(n)
#     if new.isnumeric():  # O(n)
#         new = int(new) if direction else -int(new) # O(n)
#         if new < -2147483648:
#             return -2147483648
#         elif new > 2147483647:
#             return 2147483647
#         return new
#     return 0

# Time complexity is O(4n) amounts to O(n) 




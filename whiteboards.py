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


# def moveZeroes(nums):
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             nums.append(0)
#             nums.remove(nums[i])
#             i -= 1
#         else:
#             continue
#     return nums
                

# print(moveZeroes([0, 1, 0, 3, 12]))



# def plusOne(digits):
#         num = ""
#         for i in digits:
#             num += str(i)
#         new_num = int(num) + 1
#         print(new_num)
#         new_list = [int(num) for num in str(new_num)]
#         print(new_list)
#         return new_list

# print(plusOne([9, 9]))




# given an array of integers sorted in non-decreasing order, find the starting and ending position of a given target value. if target not found in the array, return [-1, -1]

# ex:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# def start_end(list1, target):
#     indices = []
#     for i in range(len(list1)):
#         if list1[i] == target:
#             indices.append(i)
#     if indices == []:
#         return [-1, -1]
#     else:
#         return indices


# print(start_end([], 0))



# def anagrams(test, words):
#     matches = []
#     for word in words:
#         if sorted(word) == sorted(test):
#             matches.append(word)
#     return matches

# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))



# def valid_parentheses(string):
#     left = 0
#     right = 0
#     if string == "":
#         return True
#     if string[0] == ")" or string[-1] == "(":
#         return False
#     if string.count('(') != string.count(')'):
#         return False
#     for i in range(len(string)):
#         if string[i] == "(":
#             left += 1
#         elif string[i] == ")":
#             right += 1
#         if right > left:
#             return False
#     return True


# print(valid_parentheses("()test()"))


# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.

# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutivedays.
# Return true if the student is eligible for an attendance award, or false otherwise.

# s = "PPALLP"
s = "PPALLL"

def award(str1):
    for i in range(len(str1)):
        if str1[i] == 'L':
            if str1[i+1] == 'L' and str1[i+2] == 'L':
                return False
    if str1.count('A') < 2:
        return True
    return False


print(award(s))


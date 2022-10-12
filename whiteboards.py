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
# s = "PPALLL"

# def award(str1):
#     for i in range(len(str1)):
#         if str1[i] == 'L':
#             if str1[i+1] == 'L' and str1[i+2] == 'L':
#                 return False
#     if str1.count('A') < 2:
#         return True
#     return False


# print(award(s))

# rec = {"flour": 500, "sugar": 200, "eggs": 1}
# avail = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

# # rec = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# # avail = {"sugar": 500, "flour": 2000, "milk": 2000}

# def cakes(recipe, available):
#     cake_count = []
#     for key, value in recipe.items():
#         if key not in available.keys():
#             return 0
#     for key, value in recipe.items():
#         print(key)
#         print(available[key], recipe[key])
#         cake_count.append(available[key] // recipe[key])
#     print(cake_count)
#     return min(cake_count)

# print(cakes(rec, avail))



# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# def is_palindrome(str1):
#     # while loop and .remove to remove non alphanumeric
#     # use .lower()
#     # check original string against the reverse str1[::-1]
#     str2 = ""
#     for i in str1:
#         if i.isalnum() is True:
#             str2 += i 
#     lowered = str2.lower()
#     print(lowered)
#     if lowered == lowered[::-1]:
#         return True
#     return False

# print(is_palindrome("race a car"))

# 9/28/22

# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ithathlete.

# Example 1:
# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
# Example 2:
# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

# def placements(arr1):
#     sort_arr = sorted(arr1, reverse=True)
#     for i in range(len(arr1)):
#         if arr1[i] == sort_arr[0]:
#             arr1[i] = "Gold Medal"
#         elif arr1[i] == sort_arr[1]:
#             arr1[i] = "Silver Medal"
#         elif arr1[i] == sort_arr[2]:
#             arr1[i] = "Bronze Medal"
#         else:
#             arr1[i] = str(sort_arr.index(arr1[i])+1)
#     return arr1


# print(placements([5, 4, 3, 2, 1, 6]))


# You are given an array of words. Your task is to check if a permutation of each word has occurred earlier in the list -- if so, remove that word from the array, if not, keep it in the array. NOTE: A permutation is a word of the same length with the same characters -- they can be in any order (ie. "code" and "ocde")

# Example:
# words = ['code','doce','framer','frame','ocde']
# Output: ['code','framer','frame']
# Explained:
# 'code' is the first element in the array, not preceded by any permutations, so keep it
# 'doce' is a permutation of 'code', so remove it

# def isPerm(arr1):
#     # loop through array
#     # for each word, sort it, check if sorted word in already kept words array
#     # if so, continue, if not, add to final arr
#     kept = []
#     final = []
#     for i in arr1:
#         if ''.join(sorted(i)) in kept:
#             continue
#         else:
#             kept.append(''.join(sorted(i)))
#             final.append(i)
#     return final

    
# print(isPerm(['code','doce','framer','frame','ocde']))


# def reverse_words(str1):
#     reversed_word = []
#     words_list = [i for i in str1.split()]
#     print(words_list)
#     for i in words_list:
#         i = i[::-1]
#         print(i)
#         reversed_word.append(i)
#     return reversed_word

# print(reverse_words("reverse these words"))


# def maxPoints(points):
#         if len(points) < 2:
#             return len(points)
#         sort_points = sorted(points, key=lambda x: x[0])
#         print(sort_points)
#         clean_x = []
#         final_points = []
#         x_diff = []
#         y_diff = []
#         x_step = 0
#         for i in range(len(sort_points)-1):
#             x_diff.append(sort_points[i][0]-sort_points[i+1][0])
#         print(x_diff)
#         for i in x_diff:
#             if x_diff.count(i) > x_step:
#                 x_step = i
#         print(x_step)
#         for i in range(len(sort_points)-1):
#             if sort_points[i][0]-sort_points[i+1][0] == x_step:
#                 clean_x.append(sort_points[i])
#         if sort_points[-2][0]-sort_points[-1][0] == x_step:
#             clean_x.append(sort_points[-1])
#         y_step = 0
#         for i in range(len(clean_x)-1):
#             y_diff.append(clean_x[i][1]-clean_x[i+1][1])
#         print(y_diff)
#         for i in y_diff:
#             if y_diff.count(i) > y_step:
#                 y_step = i
#         print(y_step)
#         i = 0
#         while i < len(clean_x)-1:
#             if clean_x[i][1]-clean_x[i+1][1] == y_step:
#                 final_points.append(clean_x[i])
#                 i += 1
#             else:
#                 final_points.append(clean_x[i])
#                 i +=2
#         if clean_x[-2][1]-clean_x[-1][1] == y_step:
#             final_points.append(clean_x[-1])
#         return len(final_points)

# print(maxPoints([[0,0],[2,2],[-1,-1]]))



# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0

# def stones_to_jewels(jwls, stns):
#     count = 0
#     for i in stns:
#         if i in jwls:
#             count += 1
#     return count


# print(stones_to_jewels("z", "ZZ"))



# 10/12/22
# Given an integer n, return any array containing n unique integers such that they add up to 0.

# Example 1:
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:
# Input: n = 3
# Output: [-1,0,1]
# Example 3:
# Input: n = 1
# Output: [0]

def sum_zero(n):
    final = []
    if n == 1:
        return [0]
    if n == 3:
        return [-1, 0, 1]
    if n == 5:
        return [-1, 1, 0, -2, 2]
    if n % 2 == 0:
        for i in range(1, int(n/2 + 1)):
            final.append(0-i)
            final.append(0+i)
    else:
        for i in range(1, int((n-3)/2)+1):
            final.append(0-i)
            final.append(0+i)
        final.append(0-n)
        final.append(n//2)
        final.append((n//2)+1)

    return final, sum(final)

print(sum_zero(1))

# https://leetcode.cn/problems/palindrome-number/

def is_palindrome(num):
    nums = str(num)
    length = len(nums)

    for i in range(length):
        if nums[i] != nums[length - i - 1]:
            return False
    return True





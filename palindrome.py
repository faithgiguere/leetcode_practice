"""Determine whether an integer is a palindrome."""

# Using strings
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes do to sign
        if x < 0:
            return False
        else:
            x_str = str(x)
            return x_str == x_str[:-1]

# Without using strings
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be a palindrome due to sign
        if x < 0:
            return False
        # Numbers ending in 0 (exluding 0) cannot be a palindrome
        # as no other number leads with 0
        if x % 10 == 0 and x != 0:
            return False

        # Get the second half of int to compare to first
        second_half = 0
        while x > second_half:
            # Store last digit of x one by one and take it off x
            # Must caste to int to prevent floats
            second_half = int(second_half * 10 + x % 10)
            x = int(x/10)

        return x == second_half or x == int(second_half/10)

"""Given an array of integers, return indices of the two numbers such that they add up to a specific target."""

class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        # Store value, index in dict with value as key for quick lookup.
        # Duplicates will be removed, but found when iterating through nums later.
        a = {v: i for i, v in enumerate(nums)}
        for i, num in enumerate(nums):
            complement = target - num
            # Look for complement and check that it is not itself
            if a.get(complement) and a[complement] != i:
                return (i, a[complement])

"""Given an integer array nums, find the contiguous subarray (containing
at least one number) which has the largest sum and return its sum."""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:    
        # Largest sum value and current sum value
        largest = nums[0]
        curr_sum = nums[0]
        
        for i in range (1, len(nums)):
            # If current total is greater than current
            # subarray's total, start subarray over
            if nums[i] > curr_sum and curr_sum < 1:
                curr_sum = nums[i]
            # Else add current value to sum
            else:
                curr_sum += nums[i]
                
            # Compare current total against largest
            # and replace if current is greater
            if curr_sum > largest:
                largest = curr_sum
                
        return largest

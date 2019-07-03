"""Given a sorted array nums, remove the duplicates in-place such that 
    each element appear only once and return the new length."""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
                i -= 1
            i += 1

        return len(nums)

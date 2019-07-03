"""Given a string, find the length of the longest substring without repeating characters."""

class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        seen = {}
        start_index = 0
        # If string is not empty, minimum length will be at least 1
        max_length = 1 if s else 0
        for i, c in enumerate(s):
            # If character has already been seen and added to dict,
            # move new start position to char after previously seen char
            if seen.get(c, -1) >= start_index:
                start_index = seen[c] + 1
            # Otherwise char is new so add char to seen
            seen[c] = i            
            # If substring found is longer than current longest found,
            # update max length
            if i + 1 - start_index > max_length:
                max_length = i + 1 - start_index
        return max_length

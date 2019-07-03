"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid."""

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        closers = []
        for c in s:
            # If char is an opening bracket, push closing pair onto stack
            if c in pairs.keys():
                closers.append(pairs[c])
            # If no chars in closers or current char does not match
            # current closing bracket, string is not valid
            elif not closers or not closers.pop(-1) == c:
                return False
        # If anything left in closers, it was not closed and an invalid string.
        # Otherwise string is valid.
        return not closers

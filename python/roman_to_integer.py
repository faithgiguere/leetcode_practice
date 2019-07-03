"""Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999."""

class Solution:
    def romanToInt(self, s: str) -> int:
        letter_value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total_value = 0
        indexes_seen = []
        
        # If string is empty, value is 0
        if not s:
            return 0
        
        for i, letter in enumerate(s[:-1]):
            if i in indexes_seen:
                continue
            # If letter value is greater than the next, it is not a 4, 9 etc.
            # so add value as is to total
            if letter_value[letter] >= letter_value[s[i+1]]:
                total_value += letter_value[letter]
            # Else value is equal to the next value minus the current
            else:
                total_value += (letter_value[s[i+1]] - letter_value[letter]) 
                # Add indexes to seen so we don't add next value again
                indexes_seen += [i, i+1]
        
        # Check last value, add to total if index not in seen
        if len(s) - 1 not in indexes_seen:
            total_value += letter_value[s[-1]]
                
        return total_value

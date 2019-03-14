""" Given a 32-bit signed integer, reverse digits of an integer. 
    For the purpose of this problem, assume that your function returns
    0 when the reversed integer overflows. """

class Solution:
    def reverse(self, x: 'int') -> 'int':
        neg = x < 0
        
        # Take the absolute value of x
        x = abs(x)
        
        # Str x and convert to list
        x = list(str(x))
        
        # Reverse the list
        x.reverse()
        
        # Convert back to string, then back to integer
        x = int(''.join(x))
        
        if x > 2147483648:
            return 0
        
        # Add the sign back
        x = -x if neg else x
        
        return x

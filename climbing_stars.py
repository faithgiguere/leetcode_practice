"""You are climbing a stair case. It takes n steps to reach to the top.
   Each time you can either climb 1 or 2 steps. In how many distinct 
   ways can you climb to the top?"""

   class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 1: return 1
        if n == 2: return 2
        
        one_before = 2
        two_before = 1      
        total = 3
        
        # For each num of steps over 2, the total possible ways is a sum
        # of the two previous step totals
        for num in range(3, n+1):
            total = one_before + two_before
            two_before = one_before
            one_before = totals
            
        return total

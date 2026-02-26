class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0 :
            return n
            
        else:
            return 2 * n

#Time Complexity: O(1)
#Space Complexity: O(1)
#minutes spent: 2 minutes
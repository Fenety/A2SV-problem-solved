class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        
        for num in range(left, right + 1):
            
            covered = False  
            
            for start, end in ranges:
                
                if start <= num <= end:
                    covered = True
                    break  
            
            if not covered:
                return False
        
        return True
    
    #Time Complexity: O((right - left + 1) * len(ranges))
    #Space Complexity: O(1)
    #minutes spent: 31 minutes

   
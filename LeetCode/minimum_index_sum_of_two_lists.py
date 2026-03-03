class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index_map = {}
        
        for i, n in enumerate(list1):
            index_map[n] = i
        
        min_sum = float('inf')
        ans = []
        
        for j, n in enumerate(list2):
            if n in index_map:
                current_sum = j + index_map[n]
                
                if current_sum < min_sum:
                    min_sum = current_sum
                    ans = [n]
                elif current_sum == min_sum:
                    ans.append(n)
        
        return ans
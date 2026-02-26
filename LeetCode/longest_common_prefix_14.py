class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""

        for i in range(len(strs[0])):
            for s in strs:
                if s[i] != strs[0][i] or i == len(s):
                    return ans
            ans += strs[0][i]

        return ans

#time complexity : O(n * m)
#space complexity : O(m)
#time : 33 min
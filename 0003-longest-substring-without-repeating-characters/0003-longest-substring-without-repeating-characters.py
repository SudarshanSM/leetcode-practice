class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        com = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            current = s[right]
            if current in com and com[current] >= left:
                left = com[current] + 1
            com[current] = right
            max_length = max(max_length, right - left + 1)
        return max_length

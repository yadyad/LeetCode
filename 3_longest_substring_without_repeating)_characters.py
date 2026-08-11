class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_length = 0
        l = 0
        for r,c in enumerate(s):
            if c in last_seen.keys() and last_seen[c]>=l:
                l = last_seen[c] + 1
            max_length = max(max_length, r-l+1)
            last_seen[c] = r
        return max_length


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
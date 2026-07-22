class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        count_t ={}
        if len(s) != len(t):
            return False
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        for i in count.keys():
            if i not in count_t.keys():
                return False
            if count[i] != count_t[i]:
                return False
        return True
s = Solution()
print(s.isAnagram("anagram", "nsgaram"))
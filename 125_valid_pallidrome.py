
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = []
        for i in s:
            if i.isalnum():
                new.append(i.lower())
        return new == new[::-1]

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
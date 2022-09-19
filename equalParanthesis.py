class Solution:
    def isValid(self,s: str) -> bool:
        a = []
        dict = {
            '{':'}',
            '(':')',
            '[':']'
        }
        for i in s:
            if i in dict.keys():
                a.append(i)
            elif i in dict.values():
                if a:
                    if (dict.get(a.pop()) != i):
                        return False
                else:
                    return False
        return True
sol = Solution()
s = "()"
print(sol.isValid(s))
from scipy.stats import false_discovery_control
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        code_p = [0 for i in range(26)]
        code_s = [0 for i in range(26)]
        if len(s) < len(p):
            return result
        i,j = 0,len(p)-1
        for k in range(len(p)):
            index = ord(p[k]) - ord('a')
            code_p[index] += 1
        for k in range(len(p)):
            index = ord(s[k]) - ord('a')
            code_s[index] += 1
        while j<len(s):
            if code_p== code_s:
                result.append(i)
            #inserting next element to window
            j+=1
            if j>=len(s):
                return result
            index = ord(s[j]) - ord('a')
            code_s[index] += 1

            # removing first element from window

            index = ord(s[i]) - ord('a')
            code_s[index] -= 1
            i += 1

        return result

s = Solution()
print(s.findAnagrams("cbaebabacd","abc"))
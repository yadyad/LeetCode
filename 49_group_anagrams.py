from typing import List

class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(a, b):
            if len(a) != len(b):
                return False
            else:
                return sorted(a) == sorted(b)


        if strs == []:
            return [[""]]
        output = []
        while(len(strs) > 0):
            temp = []
            s = strs.pop(0)
            temp.append(s)
            for i in range(len(strs) - 1, -1, -1):
                if isAnagram(s, strs[i]):
                    temp.append(strs.pop(i))
            output.append(temp)
        return output

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in dic:
                dic[key] = [word]
            else:
                dic[key].append(word)
        return list(dic.values())

s = Solution()
print(s.groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))
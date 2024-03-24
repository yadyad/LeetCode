from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        def dfs(word, accumulated, collected):
            if ''.join(accumulated) in strs:
                collected.append(''.join(accumulated))
                return

            for i, val in enumerate(word):
                accumulated.append(val)
                word.pop(i)
                dfs(word, accumulated, collected)
                word.insert(i, val)
                accumulated.pop()

        for i,val in enumerate(strs):
            collected_words = []
            dfs(list(val), [], collected_words)
            res.append(collected_words)
            for j,value in enumerate(strs):
                if value in collected_words:
                    strs.pop(j)
        return res
    def getSignature(self, s: str) -> str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        return ''.join(result)

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        result = []
        groups = defaultdict(list)

        for s in strs:
            groups[self.getSignature(s)].append(s)
        print(groups)
        result.extend(groups.values())

        return result


l = ["eat", "tea", "tan", "ate", "nat", "bat"]
print([il[2] for il in l])

S = Solution()
print(S.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))

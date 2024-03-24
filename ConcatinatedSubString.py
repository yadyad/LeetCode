from typing import List, Optional


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        strLen = len(s)
        noOfWords = len(words)
        lenWords = len(words[0])
        result = []
        for i in range(0, strLen):
            temp = []
            for k in words:
                temp.append(k)
            count = 0
            j = i
            it = 0
            if strLen - i < noOfWords * lenWords:
                break
            while it < noOfWords:
                it += 1
                if s[j:j + lenWords] in temp:
                    count += 1
                    temp.remove(s[j:j + lenWords])
                    j += lenWords
                else:
                    break
            if (count == noOfWords):
                result.append(i)
        return result


sol = Solution()
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))

import numpy as np
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in zip(*str):
            if(len(set(i))==1):
                result = result + i[0]
            else:
                return result
        return result       

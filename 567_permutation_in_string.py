from scipy.stats import false_discovery_control


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_code = [0 for _ in range(26)]
        s2_code = [0 for _ in range(26)]
        for i, c in enumerate(s1):
            index = ord(c) - ord('a')
            s1_code[index] += 1
        i,j = 0,len(s1)-1
        for k in range(len(s1)):
            index = ord(s2[k]) - ord('a')
            s2_code[index] += 1

        print(s1_code, s2_code)
        while j < len(s2):
            if s1_code == s2_code:
                return True
            else:
                #deletion of last index
                del_index = ord(s2[i]) - ord('a')
                s2_code[del_index] -= 1
                #updating index
                i+=1
                j+=1
                #insertion of new index
                ins_index = ord(s2[j]) - ord('a')
                s2_code[ins_index] += 1
        return False
s = Solution()
print(s.checkInclusion("adc","dcda"))
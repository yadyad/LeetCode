from collections import OrderedDict
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            number = self.countAndSay(n-1)
            return self.count(number)


    def count(self,num1: int): 
        num = str(num1)
        count = 0
        if(len(num)<=0):
            return ""
        value = num[0]
        l = []
        for i in num:
            if value == i:
                count +=1
            else:
                l.append((value,count))
                count = 0
                value = i
            l.append((value,count))
        new_num = str()    
        for i,j in l:
            new_num = new_num + str(j)
            new_num = new_num + i
        return new_num

    
sol = Solution()
print(sol.countAndSay(4))
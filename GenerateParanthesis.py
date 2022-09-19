from doctest import OutputChecker


class Solution:
    
    def generateParenthesis(self, n: int):
        print("Entering Function")
        output = set()
        if(n == 1):
            return ["()"]
        else:
            for i in self.generateParenthesis(n-1).copy():
                output.add(i+"()")
                output.add("("+i+")")
                output.add("()"+i)
                
        return output
        
            
    
        
sol = Solution()
out = sol.generateParenthesis(4)
for i in out.copy():
    print(i)
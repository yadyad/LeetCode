import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []
        for token in tokens:
            if token == '+':
                b = st.pop()
                a = st.pop()
                st.append(int(a) + int(b))
            elif token == '-':
                b = st.pop()
                a = st.pop()
                st.append(int(a) - int(b))
            elif token == '*':
                b = st.pop()
                a = st.pop()
                st.append(int(a) * int(b))
            elif token == '/':
                b = st.pop()
                a = st.pop()
                st.append(math.trunc(int(a) / int(b)))
            else:
                st.append(token)
            print(f"current stack: {st}")
        return st.pop()

s = Solution()
print(6//-132)
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
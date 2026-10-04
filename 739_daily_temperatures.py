class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        st = []
        result = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            if len(st) == 0:
                st.append(i)
            else:
                while len(st) > 0:
                    last = st.pop()
                    if temperatures[last] < temperatures[i]:
                        result[last] = i - last
                    else:
                        st.append(last)
                        break
                st.append(i)

        return result

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
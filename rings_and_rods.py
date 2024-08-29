class Solution:
    def countPoints(self, rings: str) -> int:
        print(rings[0])
        rods_set = [set() for i in range(10)]
        color_set = {'R', 'G', 'B'}
        i = 0
        while(i < len(rings)):
            rods_set[int(rings[i+1])].add(rings[i])
            i+=2
        count = 0
        for i in range(10):
            if rods_set[i] == color_set:
                count+=1
        return count

    def countPoints_best_solution_python(self, ring: str) -> int:
        c = 0
        for i in range(10):
            i = str(i)
            if "R" + i in ring and "G" + i in ring and "B" + i in ring:
                c += 1
        return c

s = Solution()
print(s.countPoints("B0B6G0R6R0R6G9"))
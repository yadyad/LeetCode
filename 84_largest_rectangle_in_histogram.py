class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        largest_area = -1
        for i,height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                top = stack.pop()
                area = top[0] * (i - top[1])
                if area > largest_area:
                    largest_area = area
                start = top[1]
            stack.append((height, start))
            print(f"stack: {stack}, counter: {start}, area: {largest_area}")
        length = len(heights)
        for height,start in stack:
            area = height * (length - start)
            if area > largest_area:
                largest_area = area
            print(f"length: {length}, height: {height}area: {area}")
        return largest_area
s= Solution()
s.largestRectangleArea([3,6,5,7,4,8,1,0])

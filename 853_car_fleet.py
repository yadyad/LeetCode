class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # last_car_curr_pos = -1
        # last_car_curr_pos_index = -1
        # for i in range(len(position)):
        #     if position[i] > last_car_curr_pos:
        #         last_car_curr_pos = position[i]
        #         last_car_curr_pos_index = i
        # print("last position initially", last_car_curr_pos)
        # dist_to_finish_last_car = target - last_car_curr_pos
        # time_in_hour_to_finish = dist_to_finish_last_car // speed[last_car_curr_pos_index]
        # print("time to finsih", time_in_hour_to_finish)
        # pos_when_finish = []
        # for i in range(len(position)):
        #     pos_when_finish.append(position[i]+speed[i]*time_in_hour_to_finish)
        # print("final position", pos_when_finish)

        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

s = Solution()
print(s.carFleet(15,[10,8,0,5,3],[2,4,1,1,3]))
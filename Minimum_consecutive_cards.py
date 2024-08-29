from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        counter = {}
        _min = float('inf')
        for i, val in enumerate(cards):
            if val in counter:
                _min = min(i - counter[val] + 1, _min)
                counter[val] = i
            else:
                counter[val] = i

        return _min if _min < float('inf') else -1


class TimeMap:

    def __init__(self):
        self.key_value_map = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        list_value = self.key_value_map.get(key, [])
        list_value.append((timestamp, value))
        self.key_value_map[key] = list_value
    def get(self, key: str, timestamp: int) -> str:
        if key in self.key_value_map.keys():
            list_value = self.key_value_map[key]
            start, stop = 0, len(list_value)-1
            value = ""
            while start <= stop:
                mid = start + (stop - start) // 2
                if list_value[mid][0] == timestamp:
                    value = list_value[mid][1]
                    break
                elif list_value[mid][0] < timestamp:
                    start = mid + 1
                    value = list_value[mid][1]
                else:
                    stop = mid - 1
            return value
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
set('foo','bar',)
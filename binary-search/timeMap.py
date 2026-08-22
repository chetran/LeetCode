#!/usr/bin/env python3

class TimeMap:

    def __init__(self):
       self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        element = (value, timestamp)
        if not key in self.data:
            self.data[key] = [element]
        elif self.data[key][-1][1] == timestamp:
            self.data[key][-1] = element
        else:
            self.data[key].append(element)

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.data:
            return ""
        values = self.data[key]
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2 
            if values[m][1] > timestamp:
                r = m - 1
            else:
                l = m + 1
        return values[r][0] if r >= 0 else ""

if __name__ == '__main__':
    t = TimeMap()
    t.set("alice", "happy", 1)
    print(t.get("alice", 1))
    print(t.get("alice", 2))
    t.set("alice", "sad", 3)
    print(t.get("alice", 1))

    print(t.data)
    

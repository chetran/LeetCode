# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Use the EEF algorithm, so sort by earliest end
# Make the left most interval the focus
# Iterate through the sorted list, if the item intersect increment counter, else make it as the new focus

# Since we need to sort, it will take O(n*log(n)), but algorithm itself is O(n).

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval : interval[1])
        x = intervals[0]
        res = 0
        for interval in intervals[1:]:
            if interval[0] < x[1]:
                res += 1
                continue
            x = interval
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]) == 1)
    print(sol.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]) == 2)
    print(sol.eraseOverlapIntervals(intervals = [[1,2],[2,3]]) == 0)

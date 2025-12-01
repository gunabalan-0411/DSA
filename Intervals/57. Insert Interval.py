from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # If new interval's end LESS than old one's starting
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res +  intervals[i:]
            # If new interval's starting MORE than old one's end
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # otherwise it must be overlap
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # Shouldn't append as stills there might be some overlap
        res.append(newInterval)
        return res

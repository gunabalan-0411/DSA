from typing import List
class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Its better to sort the list first
        intervals = sorted(intervals, key = lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # work on easy skip conditions
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
                continue
            else:
                # We keep on merging otherwise we append and focus on that one in above
                res[-1] = [
                    min(res[-1][0], intervals[i][0]), 
                    max(res[-1][1], intervals[i][1])
                ]
        return res

        
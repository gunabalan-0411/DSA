from typing import List
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Attaching the index before sorting it
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key=lambda t: t[0])

        res, minHeap = [], []
        i, time = 0, 0

        while minHeap or i < len(tasks):
            # adding tasks to minHeap
            while i < len(tasks) and time >= tasks[i][0]:
                # adding processing time, its index
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]) )
                i += 1
            # if there is no tasks, fastforward time to current process arrival time
            if not minHeap:
                time = tasks[i][0]
            else:
                processing_time, index = heapq.heappop(minHeap)
                time += processing_time
                res.append(index)
        return res



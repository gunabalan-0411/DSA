from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 0->1->3->2->4->2->4 ... loop
        # Phase 1: finding the loop starting point
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: finding the duplicate
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow

print(Solution().findDuplicate(nums = [1,3,4,2,2]))
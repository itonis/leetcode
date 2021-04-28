class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        ret = []
        queue = []
        for i in range(n):
            while queue and queue[0] <= i - k:
                queue.pop(0)
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                ret.append(nums[queue[0]])
        return ret

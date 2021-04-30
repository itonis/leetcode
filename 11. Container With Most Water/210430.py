class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        l = 0
        r = len(height) - 1
        while l < r:
            h = min([height[l], height[r]])
            a = (r - l) * h
            mx = max([mx, a])
            if height[l] < height[r]:
                while height[l] <= h and l < r:
                    l += 1
            else:
                while height[r] <= h and l < r:
                    r -= 1
        return mx

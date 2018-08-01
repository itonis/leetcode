class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        sub = self.permute(nums[1:])
        ret = []
        for per in sub:
            for i in range(len(per)+1):
                ret.append(per[:i]+[nums[0]]+per[i:])
        return ret
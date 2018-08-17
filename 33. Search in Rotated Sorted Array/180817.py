class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        n, m = 0, len(nums)
        if nums[0]>nums[-1]:
            # Searching Pivot Position
            pivot = (nums[0]+nums[-1])/2
            while m>n+1:
                i = (n+m)//2
                if nums[i]>pivot:
                    n = i
                else:
                    m = i

            # Out of range
            if target<nums[m] or target>nums[n]:
                return -1
            # Pick searching range
            if target > pivot:      # Larger than pivot => lower part
                m = n+1
                n = 0
            elif target < pivot:    # Smaller than pivot => higher part
                n = m
                m = len(nums)
            else:                   # Equals pivot => not existing
                return -1
        
        # Binary Search
        while m>n+1:
            i = (n+m)//2
            if nums[i]>target:
                m = i
            elif nums[i]<target:
                n = i
            else:
                return i
        if nums[(n+m)//2]==target:
            return (n+m)//2
        return -1
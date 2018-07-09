class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        B = dict()
        for ele in A:
            counts = 1
            for div in B:
                if ele/div in B:
                    counts = counts + B[div]*B[ele/div]
            B[ele] = counts
        return sum(B.values())%(10**9+7)
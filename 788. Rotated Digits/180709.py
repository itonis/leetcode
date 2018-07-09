class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ret = 0
        for i in range(2,N+1):
            if "3" in str(i) or "4" in str(i) or "7" in str(i):
                continue
            if "2" in str(i) or "5" in str(i) or "6" in str(i) or "9" in str(i):
                ret += 1
        
        return ret
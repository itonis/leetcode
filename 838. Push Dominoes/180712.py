class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        pushing = -1
        darr = [d for d in dominoes]
        for i in range(len(darr)):
            if darr[i] == "L":
                pushing = -1
            elif darr[i] == "R":
                pushing = 0
            elif pushing>=0:
                pushing += 1
                darr[i] = pushing
                
        pushing = 0
        for i in range(len(darr)):
            if darr[-(i+1)] == "L":
                pushing = 1
            elif darr[-(i+1)] == "R":
                pushing = 0
            elif type(darr[-(i+1)]) is int:
                if pushing:
                    darr[-(i+1)] = "L" if darr[-(i+1)]>pushing else ("R" if darr[-(i+1)]<pushing else ".")
                    pushing += 1
                else:
                    darr[-(i+1)] = "R"
            else:
                if pushing:
                    darr[-(i+1)] = "L"
        return "".join(darr)
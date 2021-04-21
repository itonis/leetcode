class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        stack = []
        n = len(num)
        for i in range(1, n // 2 + 1):
            remaining = n - i
            for j in range(1, remaining // 2 + 1):
                remainingK = remaining - j
                minK = max(i, j)
                maxK = min(remainingK, minK + 1)
                for k in range(minK, maxK + 1):
                    group = (0, i, i + j, i + j + k)
                    if self.isValidGroup(group, num):
                        stack.append(group)
        while stack:
            current = stack.pop()
            if (current[3] == n):
                return True
            child = self.getChild(current, num)
            if child:
                stack.append(child)
        return False

    def getChild(self, seps: tuple, num: str):
        i = seps[1]
        j = seps[2]
        k = seps[3]
        a = int(num[i:j])
        b = int(num[j:k])
        c = str(a + b)
        if num[k:].startswith(c):
            return (i, j, k, k + len(c))
        return None

    def isValidGroup(self, seps: tuple, num: str):
        a = num[seps[0]:seps[1]]
        b = num[seps[1]:seps[2]]
        c = num[seps[2]:seps[3]]
        if self.hasLeadingZero(a) or self.hasLeadingZero(b) or self.hasLeadingZero(c):
            return False
        return int(a) + int(b) == int(c)

    def hasLeadingZero(self, num: str):
        return len(num) != 1 and num[0] == '0'

Solution().isAdditiveNumber('111')

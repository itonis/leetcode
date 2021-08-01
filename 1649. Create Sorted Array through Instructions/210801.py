class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        tree = BIT(100001)
        result = 0
        for i in range(len(instructions)):
            current = instructions[i]
            less = tree.query(current)
            greater = i - tree.query(current + 1)
            result += min(less, greater)
            tree.update(current)
        return result % 1000000007

class BIT:
    def __init__(self, size: int):
        self.array = [0] * (size + 1)

    def query(self, n: int):
        s = 0
        while n > 0:
            # print(len(self.array), n)
            s += self.array[n]
            n -= n & -n
        return s

    def update(self, n: int):
        n += 1
        while n < len(self.array):
            self.array[n] += 1
            n += n & -n

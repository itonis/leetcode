import heapq

class Field:
    def __init__(self, matrix):

        self.matrix = [[int(c, 36) for c in l] for l in matrix]
        self.li = len(matrix[0])
        self.lj = len(matrix)
        for j in range(self.lj):
            row = self.matrix[j]
            for i in range(self.li):
                p = row[i]
                if p == 11:
                    row[i] = 1
                    self.initPos = (i, j)
                elif p == 33:
                    self.goal = (i, j)

    def getAt(self, i, j):
        if i < 0 or i >= self.li or j < 0 or j >= self.lj:
            return 0
        else:
            return self.matrix[j][i]

    def getInitialPos(self):
        return self.initPos

    def getGoal(self):
        return self.goal

    def checkFloor(self, block):
        return all([self.getAt(i, j) for i, j in block.getPositions()])

    def isGoal(self, block):
        positions = block.getPositions()
        if len(positions) == 1:
            pos = positions[0]
            return self.getAt(pos[0], pos[1]) == 33
        return False

class Block:
    dirs = ['U', 'D', 'L', 'R']
    def __init__(self, i, j, off = (0, 0)):
        self.i = i
        self.j = j
        self.off = off

    def __str__(self):
        return str([(self.i, self.j), (self.i + self.off[0], self.j + self.off[1])])

    def __repr__(self):
        return 'Block: ' + str(self)

    def __lt__(self, other):
        return self.i < other.i

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j and self.off == other.off

    def __hash__(self):
        return hash((self.i, self.j)) ^ hash(self.off)

    def steps(self):
        return [(direction, self.go(direction)) for direction in Block.dirs]

    def getPositions(self):
        if any(self.off):
            di = self.off[0]
            dj = self.off[1]
            return [(self.i, self.j), (self.i + di, self.j + dj)]
        return [(self.i, self.j)]

    def go(self, direction):
        if direction == 'U':
            ni = self.i
            nj = self.j - 1 - int(not any(self.off))
            newOff = (self.off[0], int(not any(self.off)))
        elif direction == 'D':
            ni = self.i
            nj = self.j + 1 + self.off[1]
            newOff = (self.off[0], int(not any(self.off)))
        elif direction == 'L':
            ni = self.i - 1 - int(not any(self.off))
            nj = self.j
            newOff = (int(not any(self.off)), self.off[1])
        elif direction == 'R':
            ni = self.i + 1 + self.off[0]
            nj = self.j
            newOff = (int(not any(self.off)), self.off[1])
        ret = Block(ni, nj, newOff)
        return ret

def h(field: Field, block: Block):
    des = field.getGoal()
    now = block.getPositions()[0]
    di = abs(des[0] - now[0])
    dj = abs(des[1] - now[1])
    return (di // 3) + (dj // 3)

def bfs(field, block):
    queue = [(0, block, [])]
    visited = set()
    while queue:
        _, b, path = heapq.heappop(queue)
        if b in visited:
            continue
        visited.add(b)
        if field.isGoal(b):
            return ''.join(path)
        for direction, successor in b.steps():
            if field.checkFloor(successor):
                nextCost = len(path) + 1
                nextPath = path + [direction]
                heapq.heappush(queue, (nextCost + h(field, successor), successor, nextPath))

def blox_solver(ar):
    field = Field(ar)
    blockPos = field.getInitialPos()
    block = Block(blockPos[0], blockPos[1])
    return bfs(field, block)

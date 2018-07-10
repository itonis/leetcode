def manhattanDis(p, q):
    return abs(p[0]-q[0])+abs(p[1]-q[1])

class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        radius = manhattanDis([0,0], target)
        for ghost in ghosts:
            if manhattanDis(ghost, target) <= radius:
                return False
        return True
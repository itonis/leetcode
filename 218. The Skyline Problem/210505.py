class Solution:
    def merge(self, left, right):
        ret = []
        ln = len(left)
        rn = len(right)
        li = 0
        ri = 0
        h = 0
        mh = 0
        lh = 0
        rh = 0
        while li < ln and ri < rn:
            if left[li][0] < right[ri][0]:
                pos = left[li][0]
                lh = left[li][1]
                li += 1
            elif left[li][0] > right[ri][0]:
                pos = right[ri][0]
                rh = right[ri][1]
                ri += 1
            else:
                pos = right[ri][0]
                lh = left[li][1]
                rh = right[ri][1]
                li += 1
                ri += 1
            h = max([lh, rh])
            if h != mh:
                mh = h
                ret.append([pos, h])
        if li < ln:
            ret.extend(left[li:])
        if ri < rn:
            ret.extend(right[ri:])
        return ret

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return buildings
        if len(buildings) == 1:
            building = buildings[0]
            return [[building[0], building[2]], [building[1], 0]]
        mid = len(buildings) // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return self.merge(left, right)

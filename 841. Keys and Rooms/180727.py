class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        canIn = set()
        canIn.add(0)
        stack = []
        stack.append(0)
        currentRoom = -1
        while stack:
            currentRoom = stack.pop()
            for key in rooms[currentRoom]:
                if not key in canIn:
                    stack.append(key)
                    canIn.add(key)
        return len(canIn) >= len(rooms)    
        
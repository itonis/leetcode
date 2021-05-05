class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        if not len(prerequisites):
            return True
        visited = set()
        deps = dict()
        for p in prerequisites:
            if p[0] in deps:
                deps[p[0]].append(p[1])
            else:
                deps[p[0]] = [p[1]]
        for start in deps:
            if start in visited:
                continue
            stack = [start]
            frontier = {stack[0]}
            while stack:
                c = stack[-1]
                if c in deps:
                    for dep in deps[c]:
                        if dep in visited:
                            continue
                        if dep not in frontier:
                            frontier.add(dep)
                            stack.append(dep)
                            break
                        else:
                            return False
                    if stack[-1] == c:
                        visited.add(c)
                        stack.pop()
                        frontier.remove(c)
                else:
                    visited.add(c)
                    stack.pop()
                    frontier.remove(c)
        return True

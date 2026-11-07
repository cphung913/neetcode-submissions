class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = defaultdict(list)
        for p in prerequisites:
            reqs[p[0]].append(p[1])
        
        seen = set()
        done = set()
        def check(course: int):
            if not reqs[course]: return True

            for p in reqs[course]:
                if p in done: continue
                if p in seen: return False
                seen.add(p)
                if not check(p): return False
                seen.remove(p)
            done.add(course)
            return True
                

        for i in range(numCourses):
            if not check(i): return False
            seen = set()
        return True

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        for x, y in prerequisites:
            prereqs[x].append(y)
        
        done = set()
        seen = set()
        order = []
        
        def check(course: int) -> bool: # False: cant be taken
            if course in done: return True
            if course in seen: return False

            if not prereqs[course]: # no prereqs
                done.add(course)
                order.append(course)
                return True
            
            for p in prereqs[course]: # has prereqs
                if p in done: # prereq done
                    continue
                seen.add(course)
                if not check(p): return False
                seen.remove(course)
            
            order.append(course)
            done.add(course)
            return True
        
        for i in range(numCourses):
            if not check(i): return []

        return order
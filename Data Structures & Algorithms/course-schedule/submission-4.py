class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = {}
        for i in range(numCourses):
            mapping[i] = []

        for course, prereq in prerequisites:
            mapping[course].append(prereq)

        seen = set()
        def dfs(course):
            if course in seen:
                return False
            
            seen.add(course)

            # course has no prerequisites, then can be completed
            # if mapping[course] == []:
            #     return True

            for prereq in mapping[course]:
                if not dfs(prereq): 
                    return False
            
            # mapping[course] = []
            seen.remove(course)
            return True
        
        for i in range(numCourses):
            seen.clear()
            if not dfs(i):
                return False

        return True
        
        
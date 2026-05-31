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
            
            

            # course has no prerequisites, then can be completed
            if mapping[course] == []:
                return True

            seen.add(course)

            for prereq in mapping[course]:
                if not dfs(prereq): 
                    return False
            
            mapping[course] = []
            seen.remove(course)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        
        
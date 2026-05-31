class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = {}
        for i in range(numCourses):
            mapping[i] = []

        # Build the graph (adjacency list)
        for course, prereq in prerequisites:
            mapping[course].append(prereq)

        seen = set()  # This set tracks courses in the current DFS path
        
        def dfs(course):
            if course in seen:
                return False  # We found a cycle, since the course is already in the current DFS path
            
            seen.add(course)  # Add course to the current DFS path
            
            for prereq in mapping[course]:
                if not dfs(prereq):  # If any prerequisite cannot be completed, return False
                    return False
            
            seen.remove(course)  # Remove course from the current DFS path (it has been fully processed)
            return True
        
        # Run DFS on each course
        for i in range(numCourses):
            if not dfs(i):  # If DFS returns False, it means we found a cycle
                return False

        return True  # No cycles found, all courses can be finished

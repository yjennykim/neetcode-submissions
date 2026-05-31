from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = {} # prereq -> course
        indegreeMap = {}

        # initialize prerequisite map
        for i in range(numCourses):
            adjacencyList[i] = set()
            indegreeMap[i] = 0
        
        for course, prereq in prerequisites:
            indegreeMap[course] += 1
            adjacencyList[prereq].add(course)
    
        # initialize queue, add course with no prerequisites 
        q = collections.deque()
        visited = set()
        for k in indegreeMap:
            if indegreeMap[k] == 0:
                q.append(k)

        res = []
        # while queue
        while q:
            course = q.popleft()
            visited.add(course)
            res.append(course)
            for dependentCourse in adjacencyList[course]:
                indegreeMap[dependentCourse] -= 1
                if indegreeMap[dependentCourse] == 0 :
                    q.append(dependentCourse)

        if len(res) == numCourses:
            return res
        
        return []

        
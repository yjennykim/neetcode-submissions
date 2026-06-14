from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}    # graph / adj list
        in_node = {}    # course -> int (# prereqs)

        q = deque()
        for i in range(numCourses):
            courses[i] = [] # map prereq -> class
            in_node[i] = 0
        
        for course, prereq in prerequisites:
            courses[prereq].append(course)
            in_node[course] += 1
        
        # add courses w/o prereqs into queue
        for course, num_prereqs in in_node.items():
            if num_prereqs == 0:
                q.append(course)

        processed_courses = 0
        while q:
            course = q.popleft()
            processed_courses += 1

            # decrement prereq count
            for nxt in courses[course]:
                in_node[nxt] -= 1
                if in_node[nxt] == 0:
                    q.append(nxt)

        return processed_courses == numCourses



from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def find_cycle(course_id):
            if course_state[course_id] != 0:
                return course_state[course_id] == 1

            course_state[course_id] = 1

            for dependency in graph[course_id]:
                if find_cycle(dependency):
                    return True

            course_state[course_id] = 2

            return False


        graph = [[] for _ in range(numCourses)]
        course_state = [0 for _ in range(numCourses)]

        for second, first in prerequisites:
            graph[second].append(first)

        for course_id in range(numCourses):
            if find_cycle(course_id):
                return False

        return True
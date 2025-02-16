from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def build_schedule(course_id):
            if state[course_id] != 0:
                return state[course_id] == 2

            state[course_id] = 1

            for dependency in graph[course_id]:
                if not build_schedule(dependency):
                    return False

            state[course_id] = 2
            schedule.append(course_id)

            return True

        graph = [[] for _ in range(numCourses)]
        state = [0 for _ in range(numCourses)]
        schedule = []

        for second, first in prerequisites:
            graph[second].append(first)

        for course_id in range(numCourses):
            if not build_schedule(course_id):
                return []

        return schedule
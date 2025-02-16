from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cnt_dependencies = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        schedule = []
        queue = deque()

        for second, first in prerequisites:
            graph[first].append(second)
            cnt_dependencies[second] += 1

        for course_id, cnt in enumerate(cnt_dependencies):
            if cnt == 0:
                queue.append(course_id)
                schedule.append(course_id)

        while queue:
            course_id = queue.popleft()

            for dependency in graph[course_id]:
                cnt_dependencies[dependency] -= 1

                if cnt_dependencies[dependency] == 0:
                    schedule.append(dependency)
                    queue.append(dependency)

        return schedule if len(schedule) == numCourses else []
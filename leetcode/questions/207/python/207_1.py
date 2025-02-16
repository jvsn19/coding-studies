from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def find_cycle():
            queue = deque()
            completed = 0

            for course_id, cnt_dependencies in enumerate(dependencies):
                if cnt_dependencies == 0:
                    queue.append(course_id)
                    completed += 1

            while queue:
                course_id = queue.popleft()

                for dependency in graph[course_id]:
                    dependencies[dependency] -= 1

                    if dependencies[dependency] == 0:
                        completed += 1
                        queue.append(dependency)

            return completed != numCourses


        graph = [[] for _ in range(numCourses)]
        dependencies = [0 for _ in range(numCourses)]
        
        for second, first in prerequisites:
            graph[first].append(second)
            dependencies[second] += 1

        return not find_cycle()
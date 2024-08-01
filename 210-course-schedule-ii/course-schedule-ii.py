from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        incoming=[0]*numCourses
        queue = deque()
        order=[]

        for course,pre in prerequisites:
            graph[pre].append(course)# graph = [ [] , [0] ]
            incoming[course] += 1 # incoming = [1,0]

        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)# queue | 1 | 
                
        while queue:
            course = queue.popleft()
            order.append(course) # order = 1

            for neighbor in graph[course]:
                incoming[neighbor] -= 1

                if incoming[neighbor] == 0:
                        queue.append(neighbor)

        if len(order) != numCourses:
            return []
        return order
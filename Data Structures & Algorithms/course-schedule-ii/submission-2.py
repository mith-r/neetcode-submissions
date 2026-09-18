class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        # initialize graph
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        for a,b in prerequisites:
            graph[b].append(a)

        #get counts for everything
        counts = [0]*numCourses
        for values in graph.values():
            for c in values:
                counts[c] += 1
        
        #get the queue going
        queue = deque()

        for i in range(numCourses):
            if counts[i] == 0:
                queue.append(i)
        
        while len(queue) > 0:

            currCourse = queue.popleft()
            res.append(currCourse)

            for i in graph[currCourse]:
                counts[i] -= 1
                if counts[i] == 0:
                    queue.append(i)

        return res if sum(counts) == 0 else []
        
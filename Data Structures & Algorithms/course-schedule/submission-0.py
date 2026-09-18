class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        #prereq -> class that depends on it
        for a,b in prerequisites:
            graph[b].append(a) 
        
        counts = [0] * numCourses
        for courses in graph.values():
            for course in courses:
                counts[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if counts[course] == 0:
                queue.append(course)
        
        while len(queue) > 0:
            currClass = queue.popleft()
            classUnlocks = graph[currClass]

            for c in classUnlocks:
                counts[c] -= 1
                if counts[c] == 0:
                    queue.append(c)
        
        total = 0
        for i in counts:
            total+= i
        
        return total == 0
                


        print(graph)

        


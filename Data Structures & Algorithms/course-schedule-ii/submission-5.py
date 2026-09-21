class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        res = []
        for i in range(numCourses):
            graph[i] = []
        
        #course -> prereqs
        for a,b in prerequisites:
            graph[b].append(a)

        count = [0] * numCourses
        for values in graph.values():
            for c in values:
                count[c] += 1

        queue = deque()

        for i in range(numCourses):
            if count[i] == 0:
                queue.append(i)
        
        while len(queue) > 0:
            curr = queue.popleft()
            res.append(curr)

            for i in graph[curr]:
                count[i] -= 1
                if count[i] == 0:
                    queue.append(i)
        
        return res if sum(count) == 0 else []
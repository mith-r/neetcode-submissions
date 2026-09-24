class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for c, p in prerequisites:
            #prereq -> classes it unlocks
            graph[p].append(c)
        
        queue = deque()
        result = []

        #number of prereqs a class has
        pre_count = [0] * numCourses

        for key,value in graph.items():
            for c in value:
                pre_count[c] += 1

        for c in range(len(pre_count)):
            if pre_count[c] == 0:
                queue.append(c)
                result.append(c)
        
        while len(queue) > 0:
            curr = queue.popleft()

            for i in graph[curr]:
                pre_count[i] -= 1

                if pre_count[i] == 0:
                    queue.append(i)
                    result.append(i)
        
        return result if sum(pre_count) == 0 else []







    

        
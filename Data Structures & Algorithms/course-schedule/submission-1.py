class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        #gonna use an array of length numCourses, and store the number of prerequisites each class has there. When that course becomes 0, later when doing BFS i can add it to list of finished courses. That tells me to map prerequisite to item its a prereq for

        #create outgoing graph from prereq -> classes it unlocks

        graph = defaultdict(list)
        num_prereqs = [0] * numCourses

        for prereq in prerequisites:

            graph[prereq[1]].append(prereq[0])
            num_prereqs[prereq[0]] += 1

        print(graph)
        print(num_prereqs)
        
        #now we have a graph of prereqs -> class they unlock, and list of classes with numPrereqs

        #gonna run bfs to see if everything can get hit
        #first add all courses with 0 prereqs

        stack = deque()

        for i in range(numCourses):
            if num_prereqs[i] == 0:
                stack.append(i)
        
        while len(stack) > 0:
            curr = stack.popleft()
            for i in graph[curr]:

                num_prereqs[i] -= 1

                if num_prereqs[i] == 0:
                    stack.append(i)
        
        return sum(num_prereqs) ==0
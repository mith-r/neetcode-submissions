class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        stack = deque()

        intervals = sorted(intervals)

        for interval in intervals:

            if len(stack) != 0:
                previous = stack.pop()
            
                if interval[0] <= previous[1]:
                    stack.append([min(previous[0],interval[0]),max(interval[1],previous[1])])
                    continue
                    

                stack.append(previous)
            
            stack.append(interval)
        
        return list(stack)
            

            
            

        
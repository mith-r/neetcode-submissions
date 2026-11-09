class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for left, right in intervals:
            events.append((left, 1))
            events.append((right + 1, -1))
        
        events.sort()
        max_groups = 0
        current_groups = 0
        for time, delta in events:
            current_groups += delta
            if current_groups > max_groups:
                max_groups = current_groups
                
        return max_groups
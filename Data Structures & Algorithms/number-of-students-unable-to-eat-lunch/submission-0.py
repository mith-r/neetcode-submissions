class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sc = 0 
        ss = 0

        for x in students:
            if x == 0:
                sc += 1
            else:
                ss += 1

        for x in sandwiches:

            if x == 0:
                if sc == 0:
                    return ss 
                sc -= 1
                
            else:
                if ss == 0:
                    return sc 
                ss -= 1
        return sc + ss
    



        
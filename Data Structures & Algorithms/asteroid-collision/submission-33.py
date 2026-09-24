class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        #positive is going to the right
        #negative is going to the left
        #all negatives should be on left side and 

        stack = deque()
        neg = []

        for i in asteroids:
       
            if i > 0:
                stack.append(i)
            
            #checking negative
            if i < 0:
                #if there's nothing to collide with on left side
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(i)
                
               
                else:
                    #stack is positive (should loop)
                    while len(stack) > 0 and stack[-1] > 0 and abs(stack[-1]) < abs(i):
                        #2
                        stack.pop()
                    
                    #if abs(stack[-1]) == abs(i):
                    if len(stack) > 0:
                       
                        if stack[-1] < 0:
                            stack.append(i)
                        elif abs(stack[-1]) == abs(i):
                            stack.pop()
                    else:
                        stack.append(i)
                
                    
                    #they are equal
                    
                    
            

               
                            


                        
                

        return list(stack)
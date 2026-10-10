class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        incoming = deque()

        for asteroid in asteroids:

            #case where the number is positive
            if asteroid > 0:
                incoming.append(asteroid)
                continue
            
            #case where the number is negative

            #if already negative in stack (or nothing)
            if asteroid < 0:

                if len(incoming) == 0 or incoming[-1] < 0:
                    incoming.append(asteroid)
                    continue
                
                #so now there is a positive on stack

                #if they are equal size, both break

                while len(incoming) != 0 and incoming[-1] > 0 and abs(incoming[-1]) < abs(asteroid):
                    incoming.pop()
                
                if len(incoming) == 0 or incoming[-1] < 0:
                    incoming.append(asteroid)
                    continue


                if incoming[-1] * -1 == asteroid:
                    incoming.pop()
                    continue
                    
                
    
                    
                
                    



        

        return list(incoming)


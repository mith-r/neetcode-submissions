class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #basically finding longest substring of just two characters

        counts = collections.defaultdict(int)

        L = 0
        total = 0
        result = 0
        

        for R in range(len(fruits)):
            counts[fruits[R]] += 1
            total += 1

            while len(counts) > 2:
                f = fruits[L]
                counts[f] -= 1
                total -= 1
                L += 1

                if not counts[f]:
                    counts.pop(f)



            result = max(result,total)

        return result

            

        


        
       

            


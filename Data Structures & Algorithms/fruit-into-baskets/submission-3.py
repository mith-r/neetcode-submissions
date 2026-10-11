class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        baskets = defaultdict(int)

        i = 0
        maxLength = 0

        for j in range(len(fruits)):

            baskets[fruits[j]] += 1

            while len(baskets) > 2:
                baskets[fruits[i]] -= 1
                
                if baskets[fruits[i]] == 0:
                    baskets.pop(fruits[i])
                i += 1
            
            print(baskets)

            
            maxLength = max(maxLength, j-i+1)
        
        return maxLength


        
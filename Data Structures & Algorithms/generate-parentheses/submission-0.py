class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # number of ")" must always be less than or equal to number of "("

        #at each place you can either add a "(" or add a ")" (if more (s than )s

        res = []

        def dfs(i,j,string):

            if i == 0 and j == 0:
                res.append(string)
                return
            if i > 0:
                dfs(i-1,j,string + "(")
            if j > i:
                dfs(i,j-1, string+")")
            
            return
        
        dfs(n,n,"")
        return res

            


        
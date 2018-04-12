from collections import deque
from functools import reduce


class Solution:
#as similiar as a sequence into stack, ask the release order 
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        que = ['(' for i in range(n)]
        print(que)
        result = []
        def backtrack(que,stack=[],temp=[]):
            if que:
                backtrack(que[1:],stack[:]+[")"],temp[:]+[que[0]])
            if stack:
                backtrack(que[:],stack[:(len(stack)-1)],temp[:]+[stack[-1]])
            if not que and not stack:
                result.append(reduce(lambda x, y: x+y,temp))
                return
        backtrack(que)
        return result

#optimize. It's a simple writing and same as my thought
    def generateParenthesis(self,n):
        ans = []
        def trackback(result='',left=0,right=0):
            if len(reduce==2*n):
                ans.append(reduce)
            if left<n:
                trackback(result+'(', left+1, right)
            if right<left:
                trackback(result+')', left, right+1)
        trackback()
        return ans



if True:#__name__=="main":   
    s = Solution()
    s.generateParenthesis(3)



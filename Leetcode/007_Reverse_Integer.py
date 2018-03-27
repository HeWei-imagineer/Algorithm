class Solution:
    def reverse(self, x):
    	if abs(x) < 2**32:
    		result,flag = 0,1
    		if x<0:
    			flag = -1
    		while x:
    			p = x%10
    			result = result*10 + p
    			x //= 10
    		if flag:
    			return result*flag
    		else:
    			return result
    	else:
    		return 0

s = Solution()
print(s.reverse(230))

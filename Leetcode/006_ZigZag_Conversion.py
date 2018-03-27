from functools import reduce
import itertools
class Solution:
    def convert(self, s, numRows):
    	if len(s) :
    		result = [[] for i in range(numRows)] 
    		#生成Z型迭代器
    		zz = []
    		for i in range(numRows):
    			zz.append(i)
    		for j in range(i-1,0,-1):
    			zz.append(j)
    		zz = itertools.cycle(zz)
    		
    		for i,ch in enumerate(s):
        		result[next(itertools.cycle(zz))].append(ch)
       		#循环列出列表所有值
    		table = []
    		for i in result:
        		for j in i:
        			table.append(j)
    		return reduce(lambda x,y :str(x)+str(y),table)
    	else:
    		return ""

s = Solution()
print(s.convert('',3))

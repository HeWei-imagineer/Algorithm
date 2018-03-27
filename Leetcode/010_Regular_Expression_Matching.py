# class Solution:
#     def isMatch(self, s, p):
#     	##标记*好位置,去掉*,使其作为新字符串的一个字符属性
#     	pp = ''
#     	sign = []
#     	##这里因为去了*,所以sign里标记的是新pp里*前字母的位置
#     	i=0
#     	for ch in p:
#     		if ch=='*':
#     			sign.append(i-1)
#     		else:
#     			i += 1
#     			pp = pp + ch
#     	print('sigh:{0}, pp:{1}'.format(sign,pp))
#     	i,k = 0,0
#     	while k<len(s):
#         	if i < len(pp):
#         		if s[k] == pp[i] or pp[i] == '.':
#         			if i not in sign:
#         				i += 1
#         				k+=1
#         			else:
#         				if i!=len(pp)-1 and s[k]==pp[i+1]:
#         					temp = i
#         					while k<len(s) and temp<len(pp) and s[k]==pp[temp] or pp[temp]=='.':
#         						temp += 1
#         						k += 1
#         					while k<len(s) and s[k]==pp[i]:
#         					 	k+=1
#         					i = temp
#         				else:
#         					k+=1
#         		else:
#         			if i in sign:
#         				i += 1
#         			else:
#         				print(i)
#         				return False
#         	else:
#         		break
#     	print('i:%d,k:%d'%(i,k))
#     	while i<len(pp):
#         	if i in sign:
#         		i += 1
#         	else:
#         		break 
#     	if k == len(s) and i == len(pp):
#         	return True
#     	else:
#         	return False

class Solution:
    def isMatch(self, s, p):
    #竟然可以用递归。总结一下，复杂的循环，一个兔子生了一对小兔子，每个小兔子又可以生一对小兔子，有很多层，每层又有相似的处理，求最后组合的结果
    	if not p:
    		return not s
    	flag = bool(s) and p[0] in {s[0],'.'}
    	if len(p)>=2 and p[1]=='*':
    		return (self.isMatch(s,p[2:]) or flag and self.isMatch(s[1:],p))
    	else:
    		return flag and self.isMatch(s[1:],p[1:])

s=Solution()
print(s.isMatch('aaa', 'a*a'))




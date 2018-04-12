import sys

# #n = int(sys.stdin.readline().strip())
# s = 'HHTHHH'
# s = list(s)
# count = 0
# s.insert(0,s[0])
# s.append(s[-1])
# i=1

# while i<len(s)-1:
# 	if s[i]==s[i-1] and s[i]==s[i+1]:
# 		s.pop(i)
# 		continue
# 	i += 1
# print(len(s[1:-1]))


# n = int(sys.stdin.readline().strip())
# ss = []
# for i in range(n):
# 	ss.append(sys.stdin.readline().strip())

# #ss = ['())(','))((']	
# for i in ss:
# 	count,flag = 0,0
# 	for j in i:
# 		if j=='(':
# 			count += 1
# 		else:
# 			count -= 1

# 		if count<-1:
# 			break
# 		if count==-1:
# 			flag += 1
# 	if count==0 and flag<=1:
# 		print('Yes')
# 	else:
# 		print('No')

#s = sys.stdin.readline().strip()
def legal(s,result,count,length):
	if count<length:
		count += 1
		temp = s[::-1]
		if s==temp:
			result[0] += 1
		else:
			legal(s[1:],result,count,length)
			legal(s, result,count,length)
	else:
		return 
s='xxy'	
result=[0]
legal(s,result,0,len(s))
print(result)


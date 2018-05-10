import sys

# w,n = map(int,sys.stdin.readline().strip('\n').split())

# string = []
# for i in range(n):
# 	string.append(sys.stdin.readline().strip('\n'))

# for i in string:
# 	if len(i) > w :
# 		print('too long')
# 	else:
# 		print("{:.1f}".format((w-len(i))/2))
		
n = int(sys.stdin.readline().strip('\n'))
squer1 = []
squer2 = []
for i in range(n):
	k,a,b = map(int,sys.stdin.readline().strip('\n').split())
	if k == 1:
		squer1.append([a,b])
	elif k == 2:
		squer2.append([a,b])
s1,s2 = 0,0
for i in squer1:
	
for i in squer2:
	s2 += i[0] * i[1]

if s2/(s1+s2)>3/4:
	print(s1,s2,'Y')
else:
	print(s1,s2,'N')



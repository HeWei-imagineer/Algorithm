import sys 
# def Solution():
# 	# n = sys.stdin.readline()
# 	# s = sys.stdin.readline()
# 	n = 3
# 	s='LRR'
# 	l = ['N','E','S','W']
# 	index = 0
# 	for ch in s:
# 		if ch == 'L':
# 			index -= 1
# 		elif ch == 'R':
# 			index += 1
# 	if index>=0:
# 		print(l[index%4])
# 	else:
# 		print(l[(abs(index)%4)*-1])
# 	return 0
# s=Solution()

# def Solution():
# 	# a = sys.stdin.readline().split()
# 	# print(a)
# 	a = [5,2]
# 	count = 0
# 	for x in range(a[1],a[0]+1):
# 		for y in range(a[1]+1,a[0]+1):
# 			if x%y >= a[1] :
# 				count += 1
# 	print(count)
# s=Solution()

import itertools
def Solution():
	l = 2
	r = 5
	num = [0]
	natuals = itertools.count(1,1)
	i,count = 0,0
	while i <= r:
		num.append(num[i]*10+next(natuals))
		i += 1
	for i in range(l,r+1):
		if num[i]%3 == 0:
			count += 1
	print(count)

s=Solution()
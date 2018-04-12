#在一个数组中寻找指定差值的数对，相同的数对只记一次
import itertools
def findSingelKey(l,n,k):
	count = 0
	ss = set(l)
	for i in ss:
		if ss & set([i-k]):
			count += 1
	return count

l = [1,5,3,4,]
n=5
k=2
print(findSingelKey(l, n, k))
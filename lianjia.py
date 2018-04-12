def solution(num,N,result):
	if N==3:
		for i in range(num//5+1):
			solution(num-i*5,N-1,result)
	elif N==2:
		for i in range(num//2+1):
			solution(num-i*2, N-1,result)
	elif N==1:
		result[0] += 1
	return result 


print(solution(100, 3, [0]))
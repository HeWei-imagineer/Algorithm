import sys

if __name__ == "__main__":
    # 读取第一行的n
    m,n = sys.stdin.readline().strip().split()
    m,n=int(m),int(n)
    if m%2*n==0:
    	result = []
    	for i in range(m):
    		result.append((i+1)*(-1)**(i//n+1))
    	print(sum(result))

    m,n = sys.stdin.readline().strip().split()
    m,n=int(m),int(n)
    if m%2*n==0:
    	result = 0
    	for i in range(m):
    		result = result + ((i+1)*(-1)**(i//n+1))
    	print(result)

   
	









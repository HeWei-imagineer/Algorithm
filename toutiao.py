import sys


catage = []
nums = []

n = sys.stdin.readline().strip()
normal,sp,target = map(int,sys.stdin.readline().strip().split())
print(normal,sp,target)

for i in range(2):
	line = sys.stdin.readline().strip()
	catage += list(map(int, line.split()))

for i in range(normal+sp):
	if i< normal:
		nums.append(0)
	else:
		nums.append(1)

print(catage,nums,target)

            

def match(catage,nums,target,ans = []):
	j = 0 
	while True:
		if not catage:
			return
		temp = target - j*catage[0] 
		if temp==0:
			ans[0] += 1
			break
		elif temp<0 or j==1 and nums[0]==1:
			break
		else:
			match(catage[1:],nums[1:],temp,ans)
		j += 1



ans = [0]
match(catage,nums,target,ans)
print(ans)


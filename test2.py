import sys
function SumWage(){
	#wage = sys.stdin.readline().strip('\n')
	var wage=16000
	var dic = new Map([[1:'0.03,0'],[2:'0.1,105'],[3:'0.2,555'],[4:'0.25,1005'],[5:'0.3,2755'],[6:'0.35,5505'],[7:'0.45,13505']])
	var table = [1500,4500,9000,35000,55000,80000]
	var num = wage*0.8-3500
	for (i=0,i<table.length,i++){
	    if (num<n){

			break;
			}
	}
	for i,n in enumerate(table):
		
	var temp = [float(j) for j in dic.get(i+1).split(',')]
	var tax = num*temp[0]-temp[1]
	var finalWage = int(wage*0.8 - tax)
	print(finalWage)
	return finalWage 
}

SumWage()

def IsLink():
	temp = int(sys.stdin.readline().strip('\n').split(' '))
	graph = [[0 for i in range(temp[0])] for i in range(temp[0])]
	for i in range(temp[1]):
		num = int(sys.stdin.readline().strip('\n').split(' '))
		graph[num[0]][num[1]]=graph[num[1]][num[0]]=1
	n = int(sys.stdin.readline().strip('\n'))
	point = [0 for i in n]
	for i in n:
		point[i]=int(sys.stdin.readline().strip('\n').split(' '))
	flag = 0
	l=[]
	ll=[[] for i in range(temp[0])]
	for i in range(temp[0]):
		for j in range(i:temp[0]):
			if graph[i][j]==1:
				l.append(j)
		ll[i]=l
	result = []

	for i in range(len(ll)):
		if ll[i]!=-1:
			result.append(ll[i])
			ll[i]=-1
		for j in range(len(result[-1])):
			result[-1]=result[-1]+ll[j]
			ll[j]=-1
	for i in range(len(result)):
		
		


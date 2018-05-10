import 
def dfs(graph,position):
	for i in range(len(graph)):
		if graph[position][i] == 1:
			visit(graph,position,i)
			graph[position][i] = graph[i][position] = 2
			dfs(graph,i)

def visit(graph,i,j):
	if graph[i][-1] == -1:
		print(i)
		graph[i][-1] = -2
	if graph[j][-1] == -1:
		print(j)
		graph[j][-1] = -2

def bfs(graph):
	que = 

# use the last position record isVisited
graph = [[0,1,1,0,0,0,0,0,-1],[1,0,0,1,1,0,0,0,-1],[1,0,0,0,0,1,1,0,-1],[0,1,0,0,0,0,0,1,-1],
		 [0,1,0,0,0,0,0,1,-1],[0,0,1,0,0,0,1,0,-1],[0,0,1,0,0,1,0,0,-1],[0,0,0,1,1,0,0,0,-1]]

dfs(graph,0)
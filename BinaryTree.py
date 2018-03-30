#先序
class TreeNode(object):
 	"""docstring for TreeNode"""
 	def __init__(self, val,left=None,right=None):
 		self.val = val
 		self.left = left
 		self.right = right


class Tree(object):
	"""docstring for Tree"""
	def __init__(self, root=None):
		self.root = root

	def preThreadBinaryTree(self):
		stack = []
		if self.root:
			curren = self.root
			while stack or curren:
				if curren:
					print(curren.val)
					if curren.right:
						stack.append(curren.right)
					curren = curren.left
				else:
					curren = stack.pop()
		else:
			print('Tree is null')

	def midThreadBinaryTree(self):
		stack = []
		if self.root:
			curren = self.root
			while stack or curren:
				if not curren:
					while True:
						curren = stack.pop()
						print(curren.val)
						#直到找到右孩子或栈空
						if curren.right or not stack:
							break
					curren = curren.right
					#结束条件
					if not curren:
						break
				stack.append(curren)
				curren = curren.left 
		else:
			print('Tree is null')

	def afterThreadBinaryTree(self):
		stack = []
		if self.root:
			curren = self.root
			last = None
			while stack or curren:
				if not curren:
					curren = stack[-1]
					#无右孩子，直到有右孩子
					while len(stack)>1 and not stack[-1].right :
						curren = stack.pop()
						print(curren.val)
						last = curren 
					#判断栈空否
					if not stack:
						break
					#有右孩子,直到不是上一次访问值
					while stack and stack[-1].right and stack[-1].right==last:
						curren = stack.pop()
						print(curren.val)
						last = curren
					#判断栈空否
					if not stack:
						break
					#有右孩子，而且不是上一次访问值
					if stack[-1].right and stack[-1].right!=last:
						curren = stack[-1]
						stack.append(curren.right)
						#这里出了错！！！，少了right，你的程序逻辑太容易出错
						curren = curren.right.left
						continue
				stack.append(curren)
				curren = curren.left 
		else:
			print('Tree is null')
		

if True:
	f = TreeNode('f',None,None)
	g = TreeNode('g',None,None)
	h = TreeNode('h',None,None)
	e = TreeNode('e',None,h)
	d = TreeNode('d',f,g)
	c = TreeNode('c',None,e)
	b = TreeNode('b',None,d)
	a = TreeNode('a',b,c)
	tree = Tree(a)
#	tree.preThreadBinaryTree()
#	tree.midThreadBinaryTree()
	tree.afterThreadBinaryTree()

		

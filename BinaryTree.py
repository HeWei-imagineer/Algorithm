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

	def inThreadBinaryTree(self):
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

	def postThreadBinaryTree(self):
		stack = []
		if self.root:
			curren = self.root
			while stack or curren:
				if not curren:
					while stack and stack[-1].right == curren:
						curren = stack.pop()
						print(curren.val)
					if not stack:
						break
					#如果右孩子未访问过，当前指针指向有孩子
					curren = stack[-1].right

				stack.append(curren)
				curren = curren.left 
		else:
			print('Tree is null')
		

if __name__=='__main()__':
	f = TreeNode('f',None,None)
	g = TreeNode('g',None,None)
	h = TreeNode('h',None,None)
	e = TreeNode('e',None,h)
	d = TreeNode('d',f,g)
	c = TreeNode('c',None,e)
	b = TreeNode('b',None,d)
	a = TreeNode('a',b,c)
	tree = Tree(a)
	tree.preThreadBinaryTree()
	tree.inThreadBinaryTree()
	tree.postThreadBinaryTree()

		

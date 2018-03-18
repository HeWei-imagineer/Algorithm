import pdb
from datetime import datetime, timedelta 
# >>> def triangles(n):
# 	if n<1:
# 		print('invalid num')
# 	elif n==1:
# 		print(1)
# 		return 
# 	else:
# 		i,k=0,1
# 		result = []
# 		result.append([1])
# 		while n>i:
# 			alist = []
# 			a = 0
# 			for m in result[i]:
# 				alist.append(a+m)
# 				a=m
# 			alist.append(a)
# 			result.append(alist)
# 			i += 1
# 			yield alist
			
# 	return

# >>> for t in triangles(10):
# 	print(t)

# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
# >>> 


from datetime import datetime, timedelta 
class Solution:
#l为一个待选序列，例如三个人里任选两个(无序)，则l为初始值为0（选中为1），长度为3的列表，s为2,ll为存储结果的列表,
def disorder_combination(l,s,ll,index):
	if s<1 :
		temp = []
		for i in l:
			temp.append(i)
		#因为还款不会在最后一天
		temp.append(0)
		ll.append(temp)
	else :
		if index <= len(l)-s+1 :
			for i in range(index,len(l)-s+1):
				#消除上一次循环留下的修改
				if i != index:
					l[i-1] = 0
				l[i] = 1
				#传入的位置是i，不是index
				disorder_combination(l,s-1,ll,i+1)
			#处理边界被置为1的情况
			if i == len(l)-s:
				l[i] = 0

#判断两个列表里同一位置相同的元素有多少个（忽略0）
def IsSame(l1,l2):
	k=0
	ll = []
	while k<len(l1) and k<len(l2):
		if l1[k]==l2[k] and l2[k]!=0 :
			ll.append(k)
		k += 1
	return ll

#date为开始日期，ll为封装的可能出现的违约组合
#无选择输出
def print_date_1(date,l1,l1_name,l2,l2_name):
	my_date = datetime.strptime(date,'%Y-%m-%d')
	print('one kind of situation')
	for i1 in l1:
		for i2 in l2:
			k = 0
			while k<len(i1) or k<len(i2):
				curren = my_date + timedelta(days=k)
				current_str = curren.strftime('%Y-%m-%d')
				if k<len(i1):
					if i1[k]:
						print(current_str+'-'+l1_name+'(no)')
					else:
						print(current_str+'-'+l1_name+'(ok)')
				if k<len(i2):
					if i2[k]:
						print(current_str+'-'+l2_name+'(no)')
					else:
						print(current_str+'-'+l2_name+'(ok)')
				k += 1
			print('------------------------------')

#有选择输出
def print_date_2(date,l1,l1_name,l2,l2_name):
	my_date = datetime.strptime(date,'%Y-%m-%d')	
	for i1 in l1:
		for i2 in l2:
			if len(IsSame(i1,i2))==0:
				k=0
				while k<len(i1) or k<len(i2):
					curren = my_date + timedelta(days=k)
					current_str = curren.strftime('%Y-%m-%d')
					if k<len(i1):
						if i1[k]:
							print(current_str+'-'+l1_name+'(no)')
						else:
							print(current_str+'-'+l1_name+'(ok)')
					if k<len(i2):
						if i2[k]:
							print(current_str+'-'+l2_name+'(no)')
						else:
							print(current_str+'-'+l2_name+'(ok)')
					k += 1
				print('------------------------------')

#特定输出(单纯按列表输出)			
def print_date_3(date,l1,l1_name,l2,l2_name):
	my_date = datetime.strptime(date,'%Y-%m-%d')
	print('one kind of situation')					
	for i1 in l1:
		k=0
		while k<len(i1):
			curren = my_date + timedelta(days=k)
			current_str = curren.strftime('%Y-%m-%d')
			if k<len(i1):
				if i1[k]:
					print(current_str+'-'+l1_name+'(no)')
					print(current_str+'-'+l2_name+'(no)')
				else:
					print(current_str+'-'+l1_name+'(ok)')
					print(current_str+'-'+l2_name+'(ok)')
				k += 1
		print('------------------------------')

def Solution():
	date,index,temp = '2018-4-30',0,[[0,0,0]]
	#1.同一天失信于两人	
	l_31 = [[1,0,0,0],[0,1,0,0],[0,0,1,0]]
	print('first situation of break_score=3')
	print_date_3(date,l_31,'A',l_31,'B')
	#2.一天失信于一人，另外两天失信于另一人
	l_321,l_322,my_321,my_322= [],[],[0,0,0,0], [0,0,0]
	disorder_combination(my_321, 2, l_321, index)
	disorder_combination(my_322, 1, l_322, index)
	print('second situation of break_score=3')
	print_date_2(date,l_321,'A',l_322,'B')
	print_date_2(date,l_321,'B',l_322,'A')
	#3.失信一人三次（不连续）
	l_33,my_33,l_331 = [],[0,0,0,0,0],[[1,1,1,0,0,0],[0,1,1,1,0,0],[0,0,1,1,1,0]]
	disorder_combination(my_33, 3, l_33, index)
	l_33 = [i for i in l_33 if i not in l_331]
	print('third situation of break_score=3')
	print_date_1(date,l_33,'A',temp,'B')
	print_date_1(date,temp,'A',l_33,'B')
	#1.失信一人两次
	my_21,l_21= [0,0,0,0],[]
	disorder_combination(my_21, 2, l_21, index)
	print('first situation of break_score=2')
	print_date_1(date,l_21,'A',temp,'B')
	print_date_1(date,temp,'B',l_21,'A')
	#2.对每人失信一次
	my_22,l_22 = [0,0,0],[]
	disorder_combination(my_22, 1, l_22, index)
	print('second situation of break_score=2')
	print_date_2(date,l_22,'A',l_22,'B')
	#1.失信一人一次
	my_l1,l1 = [0,0,0],[]
	disorder_combination(my_l1, 1, l1, index)
	print('one situation of break_score=1')
	print_date_1(date,l1,'A',temp,'B')
	print_date_1(date,l1,'B',temp,'A')
	
Solution()





#Longest Substring Without Repeating Characters
#it can find the specific substring

import math,logging


def lengthOfLongestSubstring(s):
	sum = set()
	count,head,k,index = 0,0,0,0
	while k<len(s) and index<len(s):
		k=index
		while k<len(s) and (s[k] not in sum):
			sum.add(s[k])
		
			k+=1
		sum = set()
		if count<k-index :
			count = k-index
			head = index
		
		index +=1
	print('count:%d'%conut)
	return s[head:(head+count)]

#just find the length, using sliding window
def lengthOfLongestSubstring_1(s):
	mysum = set()
	mydic = {}
	i,j,count=0,0,0
	while(j<len(s)):
		if s[j] not in mysum:
			mysum.add(s[j])
			mydic[s[j]] = j+1
			count = max(count,j-i+1)
		else:
			i = max(mydic.get(s[j]),i)
			mydic[s[j]] = j+1
		j += 1
	return count

#test
logging.basicConfig(level=logging.INFO)
logging.info(lengthOfLongestSubstring_1('awsdasbrt'))





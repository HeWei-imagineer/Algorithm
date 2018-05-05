# #Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# #the problem of boundary condition!!
# class Solution:
#     def swapPairs(self, head):
#     	if not head or not head.next:
#     		return head

#     	star = dump = ListNode(0)
#     	star.next = head.next
#     	while head and head.next:

#     		temp = head.next
#     		#the link of each adjacent node
#     		dump.next = temp
    		
#     		head.next = head.next.next
#     		temp.next = head
#     		#the link of each adjacent node
#     		dump = head

#     		head = head.next

#     	return star.next



if True:#__name__ == "__main()__":
	#s = Solution()
	n1 = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n5 = ListNode(5)
	n6 = ListNode(6)
	n7 = ListNode(7)
	n1.next = n3
	n3.next = n4
	n4.next = n6
	n2.next = n5
	n5.next = n7
	n7.next = n1
	temp = n2
	while temp:
		print(temp.val)
		temp = temp.next

	# l = s.swapPairs(n2)
	# while l:
	# 	print(l.val)
	# 	l = l.next
	temp = None
	head = n2
	while head:
		print('head',head.val)
		temp1 = head.next
		head.next = temp
		temp = head
		if temp1:
			head = temp1
		else:
			break
	# dump = head
	# while dump.next.next:
	# 	dump = dump.next
	# dump.next = None


	l = head
	print('result')
	while l:
		print(l.val)
		l = l.next


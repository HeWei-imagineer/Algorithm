#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #对头指针操作会出问题

        if type(head)==ListNode and head.next:
        	temp = ListNode(0)
        	temp.next = head
        	first=seach=temp
        	while n+1:
        		first = first.next
        		n -= 1
        	while first:
        		seach = seach.next
        		first = first.next
        	seach.next = seach.next.next
       		return temp.next
       
if True:#__name__=='__main()__':
	head = ListNode(None)
	n1 = ListNode(6)
	n2 = ListNode(2)
	n3 = ListNode(6)
	head.next = n1
	n1.next = n2
	n2.next = n3
	s = Solution()
	l = s.removeNthFromEnd(head,1)  
	while l:
		print(l.val)
		l = l.next     
        	

        
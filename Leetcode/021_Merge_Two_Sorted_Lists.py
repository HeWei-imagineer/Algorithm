# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


        # h1,h2=l1,l2
        # curern = ListNode(0)
        # while h1 or h2:
        # 	if h1==None:
        # 		curren.next = h2
        # 		break
        # 	elif h2==None:
        # 		curren.next = h1
        # 		break
        # 	else:
        # 		if h1.val<=h2.val:
        # 			curren.next = h1
        # 			curren = curren.next
        # 			h1 = h1.next
        # 		else:
        # 			curren.next = h2
        # 			curren = curren.next
        # 			h2 = h2.next
        # return head

        temp = curern = ListNode(0)
        while l1 and l2:
        	if l1.val<=l2.val:
        		curren.next = l1
        		l1 = l1.next
        	else:
        		curren.next = l2
        		l2 = l2.next
        	curren = curren.next
        curern.next = l1 or l2
        return temp.next





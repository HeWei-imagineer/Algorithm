#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#cool, harder ac one time 
class Solution:
    def mergeKLists(self, lists):
    	if len(lists)>1:
    		middle = len(lists)//2
    		return self.merge(self.mergeKLists(lists[:middle]),
    		self.mergeKLists(lists[middle:]))
    	else:
    		return lists

    def merge(self,l1,l2):
    	head = dump = ListNode(0)
    	while l1 or l2:
    		if not l1 or not l2:
    			dump.next = l2 if not l1 else l1 
    			break
    		elif l1.val <= l2.val:
    			dump.next = l1
    			l1 = l1.next
    		else:
    			dump.next = l2
    			l2 =l2.next
    		dump = dump.next
    	return head.next


#there is another way of comparision node one by one. it used priority queue.
from queue import PriorityQueue
def mergeKLists(self, lists):
	head = dump = ListNode(0)
	q = PriorityQueue()
	for l in lists:
		q.put((l.val,l))
	while not q.empty():
		val,node = q.get()
		dump.next = ListNode(val)
		node = node.next
		if node:
			q.put((node.val,node))
	return head.next



if True:#__name__ == "__main()__":
	s = Solution()
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
	l = s.merge(n1,None)
	while l:
		print(l.val)
		l = l.next




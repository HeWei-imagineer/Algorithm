# Definition for singly-linked list.

class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1,num2,i=0,0,0
        while(l1):
            num1 = num1 + l1.val*10**i
            l1 = l1.next
            i+=1
            
        i=0
        while(l2):
            num2 = num2 + l2.val*10**i
            l2 = l2.next
            i+=1
        num = num1+num2
        alist = []
        
        while(num//10):
            n=num%10
            alist.append(n)
            num=num//10
            
        alist.append(num) 
        i=0
        anodelist = []
        for i in alist:
            anodelist.append(ListNode(i))
        for i in range((len(anodelist)-1)):
            anodelist[i].next = anodelist[i+1]
        return anodelist[0]

    def addTwoNumbers_1(self, l1, l2):
        head = ListNode(0)
        p,q,h,temp = l1,l2,head,0
        while p or q:
            if p:
                x = p.val
            else:
                x = 0
            if q:
                y = q.val
            else:
                y = 0
            num = x + y + temp
            h.next = ListNode(num%10)
            h = h.next
            temp = num // 10
            
            if p : 
                p = p.next
            if q :
                q = q.next
        return head.next

#test
n1 = ListNode(5)
n2 = ListNode(1)
n3 = ListNode(6)
n1.next = n2
s = Solution()
ll=s.addTwoNumbers_1(n1, n3)
l = ll
while l:
    print(l.val)
    l = l.next




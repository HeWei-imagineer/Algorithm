# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #star markup the end of KGroup, star.next point to another end of KGroup. then just do reverse in ench group
        if not head or not head.next or k==1:
            return head
        star = temp = point = ListNode(0)
        count = k
        while True:
            #print(count, head.val)
            if count == k:
                if not head:
                    point.next = head
                    return star.next
                # star.next already change
                pre = head
                for i in range(k-1):
                    pre = pre.next
                    #print('pre.vl',pre.val)
                    # the left-out's length is not multiple of k
                    if not pre:
                        point.next = head
                        return star.next
                point.next = pre
                point = head
                # normalize head
                temp = head
                head = head.next
                count = 1

            count += 1
            temp1 = head.next
            head.next = temp
            temp = head
            head = temp1

s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
temp = s.reverseKGroup(n1, 2)

while temp:
    print(temp.val)
    temp = temp.next



       

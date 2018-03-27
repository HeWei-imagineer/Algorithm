class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        star,end=0,len(s)-1
        while star<end:
        	if s[star]==s[end]:
        		star += 1
        		end -=1
        	else:
        		break
        return False if star<end else True 

    def isPalindrome_1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #虽然ac，但考虑太少，负数，没注意不能有额外空间
        #so another show
        if x<0 or (x%10==0 and x!=0):
        	return False
        else:
        	revertedNum = 0
        	#这里很巧妙，倒置整数会导致overflow
        	while x > revertedNum:
        	 	revertedNum = revertedNum*10 + x%10 
        	 	x = x//10
        	if x==revertedNum or x==revertedNum//10:
        		return True
        	else:
        		return False


s = Solution()
print(s.isPalindrome_1(-2147483648))        
#Longest Palindromic Substring
#判断每一个位置是否是中心点，以及和它后一个点组合是否是中心点

#处理程序时，并列两种情况出现时，只处理了后一种情况的结果
#原因：结果处理程序块位置不当，两种情况都是可能发生的，并不是异或关系

class Solution:
    def findPalindrome(self,s,star,end):
        result = []
        while star>=0 and end<len(s):
            if s[star]==s[end]:
                star -= 1
                end += 1
            else:
                break
        result.append(end-star-1)
        #存储回文的第一个字符下标
        result.append(star+1)
        #存储回文的最后一个字符下标+1，方便后面s[result[1]:result[2]]直接返回回文内容
        result.append(end)
        return result        


    def longestPalindrome(self, s):
        result = [0]
        for i in range(len(s)):
            if i<len(s)-1 and s[i]==s[i+1]:
                star,end = i-1,i+2 
                result_temp = self.findPalindrome(s,star,end)
                if result[0]<result_temp[0]:
                	result = result_temp
            star,end = i-1,i+1 
            result_temp = self.findPalindrome(s,star,end)
            if result[0]<result_temp[0]:
                result = result_temp
        if result[0] == 1:
            return s[result[1]]
        else:
            return s[result[1]:result[2]]


#你这个方法代码冗余，逻辑上容易出错，对于回文是偶数或奇数的情况再考虑一下，就是把相同的字符绑到一起
#so当你把情况分的过多的时候，请找出他们的统一性
class Solution:
    def longestPalindrome_1(self, s):
        #记录回文长度
        count = 0
        for i in range(len(s)):
            j=i+1
            while j<len(s):
                if s[i]==s[j]:
                    j+=1
                else:
                    break
            star = i-1
            end = j
            while star>=0 and end<len(s):
                if s[star]==s[end]:
                    star -= 1
                    end += 1
                else:
                    break
            if count <end-star-1:
                count = end-star-1
                result = s[star+1:end]
        return result







ss = 'cdde'
s = Solution()
a = s.longestPalindrome_1(ss)
print(a)
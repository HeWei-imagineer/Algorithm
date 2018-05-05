class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        ev = self.eigenVal(needle)
        i,j = 0,1
        while i < len(haystack):
            #move the needle, for each compare just move the needle
            #another word, compare current haystack[i] with needle[ev[j-1]], 
            #j means last time when haystack[i] == needle[j], but now j++,i++
            j = ev[j-1]
            star = i - j
            while j < len(needle) and i < len(haystack):
                print(i,haystack[i],j,needle[j])
                if haystack[i] != needle[j]:
                    break
                i += 1
                j += 1 
            if j == len(needle):
                return star
            #hack!!!! why is there a bug here.
            elif j == 0:
                j = 1
                i += 1
        return -1

    
    def eigenVal(self,target):
        ev = [0]
        for i in range(1,len(target)):
            temp = ev[i-1]
            while True:
                if target[i] == target[temp]:
                    ev.append(temp+1)
                    break
                #when ev[temp] = temp,return 0  exemple:ccco
                elif temp==0:
                    ev.append(0)
                    break
                else:
                    #temp means length, so temp-1 when visit the prefix substring
                    temp = ev[temp-1]
        return ev

if True: #__name__=="__main()__":
	s = Solution()
	print(s.eigenVal("aabaaac"))   
	print(s.strStr("aabaaabaaac","aabaaac"))





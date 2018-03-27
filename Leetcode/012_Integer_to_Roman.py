class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # reverChart = [list1
        # list2
        # list3
        # list4]
        
        # i,s = 0,[]
        # while num:
        # 	p = num%10
        # 	if p:
        # 		s.append(reverChart[i][p])
        # 	num = num//10
        # 	i += 1
        # ss = ''
        # for i in range(len(s)-1,0,-1):
        # 	ss = ss + s[i]
        # return ss

        list1 = ["", "M", "MM", "MMM"]
        list2 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        list3 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        list4 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return list1[num//1000%10] + list2[(num%1000)//100%10] + list3[(num%100)//10%10] + list4[num%10]



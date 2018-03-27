class Solution:
    def romanToInt(self, s):
        reverChart = [
        ["", "M", "MM", "MMM"],
        ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        ]
        #细节啊！
        result = 0 
        for i,ch in enumerate(reverChart):
            for j in range(len(ch)-1,-1,-1):
                if ch[j] == s[:len(ch[j])]:
                    s = s[len(ch[j]):]
                    result = result + j * 10**(3-i)
        return result

       
s = Solution()
print(s.romanToInt("MCMXCVI"))

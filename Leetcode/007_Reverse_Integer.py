
class Solution:
    # pay attention to answer. the answer's length maybe overflow
    def reverse(self,x):
        ans = int(str(abs(x))[::-1])*((x>0)-(x<0))
        return ans if ans.bit_length() < 32 else 0

if __name__=="__main()__":
    s = Solution()
    print(s.reverse(1534236469))

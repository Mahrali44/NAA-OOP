class Solution:
   def solve(self, n):
      s ="" for i in range(n):
      s+= " "*(n-i-1)+"*"*(i+1)
      if(i<n-1):
         s+="\n"
      return s
ob = Solution()
print(ob.solve(5))
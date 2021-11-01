class Solution:
    def MissingNumber(self,array):
        n = len(array)
        total = (n+1)*(n+2)/ 2
        sum_of_A = sum(array)
        return total - sum_of_A
        
        
array = [1,4,3,2]
classes = Solution()
print(classes.MissingNumber(array))

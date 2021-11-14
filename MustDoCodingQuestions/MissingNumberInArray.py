'''
Approach 1 :
class Solution:
    def MissingNumber(self,array):
        n = len(array)
        total = (n+1)*(n+2)/ 2
        sum_of_A = sum(array)
        return total - sum_of_A
        
        
array = [1,4,3,2]
classes = Solution()
print(classes.MissingNumber(array))'''

# Approach 2 : Utilizing XOR logic 
# a1^a2^a3 ... an = a and a1^a2^a3... ^ an-1 = b
# a^b = an
def getMissingNo(a, n):
    x1 = a[0]
    x2 = 1
    
    for i in range(1, n):
        x1 = x1 ^ a[i]
        
    for i in range(2, n + 2):
        x2 = x2 ^ i
    
    return x1 ^ x2


# Driver program to test above function
if __name__=='__main__':

    a = [1, 2, 4, 5, 6]
    n = len(a)
    miss = getMissingNo(a, n) 
    print(miss)
    
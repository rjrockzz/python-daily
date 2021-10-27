'''You are given a list of n-1 integers and
 these integers are in the range of 1 to
  n. There are no duplicates in the list.
 One of the integers is missing in the list. 
 Write an efficient code to find the missing integer.'''

Approach #1 Take the sum of the n numbers and subtract it form the sum
         # of the array
class Solution:
    def missing_number(self, arr, n):
        self.arr = arr
        self.n = n
        sum_n = (n*(n+1))/2
        sum_arr = 0
        for i in arr:
            sum_arr = sum_arr + i
        return sum_n-sum_arr

i = Solution()
result = int(i.missing_number([1,3,2,5], 5))
print(result)